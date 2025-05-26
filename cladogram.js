// Modular D3.js Cladogram Visualization with Lazy Loading OTOL Support and Improved Loading Indicator

export function renderCladogram(data, options = {}) {
  const {
    container = "#tree",
    width = 1200,
    height = 800,
    nodeWidth = 180,
    tooltipId = "#tooltip",
    onNodeClick = null,
    onNodeHover = null,
    onNodeLeave = null,
    onLazyLoad = null, // function(nodeData, d3Node, doneCallback)
  } = options;

  d3.select(container).selectAll("*").remove();
  const svg = d3.select(container)
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(100,0)");

  const treeLayout = d3.tree().size([height, width - 200]);
  let root = d3.hierarchy(data);
  root.x0 = height / 2;
  root.y0 = 0;

  if (root.children) root.children.forEach(collapse);

  update(root);

  function collapse(d) {
    if (d.children) {
      d._children = d.children;
      d._children.forEach(collapse);
      d.children = null;
    }
  }

  function update(source) {
    treeLayout(root);
    const nodes = root.descendants();
    const links = root.links();
    nodes.forEach(d => d.y = d.depth * nodeWidth);

    // Remove all spinners before redraw
    svg.selectAll('.loading-spinner').remove();

    const node = svg.selectAll('g.node')
      .data(nodes, d => d.id || (d.id = Math.random()));

    const nodeEnter = node.enter().append('g')
      .attr('class', 'node')
      .attr('transform', d => `translate(${source.y0},${source.x0})`)
      .on('click', function (event, d) {
        if (event.defaultPrevented) return;

        // Lazy load children if not loaded and OTT ID is present
        if (!d.children && !d._children && d.data.ott_id && onLazyLoad) {
          showLoading(svg, d.y, d.x, d.id);
          onLazyLoad(d.data, d, (children) => {
            removeLoading(svg, d.id);
            if (Array.isArray(children) && children.length > 0) {
              d.children = children.map(child => d3.hierarchy(child));
              d.children.forEach(child => { child.parent = d; });
            }
            update(d);
          });
          return;
        }

        if (d.children) {
          d._children = d.children;
          d.children = null;
        } else {
          d.children = d._children;
          d._children = null;
        }
        update(d);
        if (onNodeClick) onNodeClick(d);
      })
      .on('mouseover', function (event, d) {
        if (onNodeHover) onNodeHover(event, d);
      })
      .on('mousemove', function (event, d) {
        if (onNodeHover) onNodeHover(event, d);
      })
      .on('mouseleave', function (event, d) {
        if (onNodeLeave) onNodeLeave(event, d);
      });

    nodeEnter.append('circle')
      .attr('r', 6)
      .attr('fill', d => d._children ? "#ccc" : "#fff")
      .attr('stroke', "steelblue")
      .attr('stroke-width', 3);

    nodeEnter.append("text")
      .attr("dy", 3)
      .attr("x", d => d.children || d._children ? -12 : 12)
      .style("text-anchor", d => d.children || d._children ? "end" : "start")
      .text(d => d.data.name);

    const nodeUpdate = nodeEnter.merge(node);
    nodeUpdate.transition()
      .duration(200)
      .attr('transform', d => `translate(${d.y},${d.x})`);

    nodeUpdate.select('circle')
      .attr('fill', d => d._children ? "#ccc" : "#fff")
      .attr('class', d => d.matched ? 'highlighted' : '');

    node.exit().transition()
      .duration(200)
      .attr('transform', d => `translate(${source.y},${source.x})`)
      .remove();

    // Links
    const link = svg.selectAll('path.link')
      .data(links, d => d.target.id);

    link.enter().insert('path', "g")
      .attr("class", "link")
      .attr("fill", "none")
      .attr("stroke", "#ccc")
      .attr("stroke-width", 2)
      .attr("d", d => {
        const o = { x: source.x0, y: source.y0 };
        return diagonal({ source: o, target: o });
      });

    link.transition()
      .duration(200)
      .attr("d", diagonal);

    link.exit().transition()
      .duration(200)
      .attr("d", d => {
        const o = { x: source.x, y: source.y };
        return diagonal({ source: o, target: o });
      })
      .remove();

    nodes.forEach(d => {
      d.x0 = d.x;
      d.y0 = d.y;
    });
  }

  function diagonal(d) {
    return d3.linkHorizontal()
      .x(d => d.y)
      .y(d => d.x)(d);
  }

  // Show a spinner or loading indicator at (y, x) for this node id
  function showLoading(svg, y, x, nodeId) {
    // Remove existing spinner for this node (safety)
    removeLoading(svg, nodeId);
    const group = svg.append("g")
      .attr("class", "loading-spinner")
      .attr("id", "spinner-" + nodeId)
      .attr("transform", `translate(${y},${x})`);
    group.append("circle")
      .attr("r", 11)
      .attr("fill", "none")
      .attr("stroke", "#bbb")
      .attr("stroke-width", 3)
      .attr("stroke-dasharray", "11,7")
      .attr("opacity", 0.7);
    group.append("text")
      .attr("y", 4)
      .attr("x", 20)
      .text("Loading...")
      .attr("fill", "#bbb")
      .attr("font-size", "12px");
    // Animate spinner (CSS handles spin)
  }

  function removeLoading(svg, nodeId) {
    svg.select(`#spinner-${nodeId}`).remove();
  }
}