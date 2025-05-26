// Tooltip utility for D3.js, now includes synonyms, sources, taxonomy path, external IDs if present
export function showTooltip(event, d, tooltipSelector = "#tooltip") {
  let html = `<strong>${d.data.name}</strong>`;
  if (d.data.rank) html += `<br><em>Rank:</em> ${d.data.rank}`;
  if (d.data.ott_id) html += `<br><em>OTT ID:</em> ${d.data.ott_id}`;
  if (d.data.taxonomy_path && d.data.taxonomy_path.length > 1) {
    html += `<br><em>Path:</em> <small>${d.data.taxonomy_path.join(" &rarr; ")}</small>`;
  }
  if (d.data.synonyms && d.data.synonyms.length > 0) {
    html += `<br><em>Synonyms:</em> ${d.data.synonyms.join(", ")}`;
  }
  if (d.data.external_ids) {
    for (const [db, id] of Object.entries(d.data.external_ids)) {
      if (db === "NCBI") {
        html += `<br><em>NCBI:</em> <a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=${id}" target="_blank">${id}</a>`;
      } else if (db === "GBIF") {
        html += `<br><em>GBIF:</em> <a href="https://www.gbif.org/species/${id}" target="_blank">${id}</a>`;
      } else {
        html += `<br><em>${db}:</em> ${id}`;
      }
    }
  }
  if (d.data.sources && d.data.sources.length > 0) {
    html += `<br><em>Sources:</em>`;
    html += d.data.sources.map(src =>
      src.startsWith("http") ?
        `<br>&nbsp;&nbsp;<a href="${src}" target="_blank">${src}</a>`
        : `<br>&nbsp;&nbsp;${src}`
    ).join('');
  }
  d3.select(tooltipSelector)
    .html(html)
    .style('display', 'block')
    .style('background', 'rgba(255,255,255,0.98)')
    .style('border', '1px solid #888')
    .style('padding', '8px')
    .style('border-radius', '6px')
    .style('pointer-events', 'none')
    .style('font-size', '15px')
    .style('left', (event.pageX + 16) + 'px')
    .style('top', (event.pageY - 16) + 'px');
}
export function hideTooltip(tooltipSelector = "#tooltip") {
  d3.select(tooltipSelector).style('display', 'none');
}