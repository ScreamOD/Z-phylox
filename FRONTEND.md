# Frontend Architecture: Tree of Life Cladogram

## Modular Structure

The frontend is organized into ES6 modules for clarity, extensibility, and scientific reproducibility.

### Module Overview

| Module            | Purpose                                            |
|-------------------|---------------------------------------------------|
| `cladogram.js`    | Core D3.js rendering and tree interaction         |
| `tooltip.js`      | Tooltip display, metadata formatting and logic     |
| `search.js`       | Search, matching, and node reveal utilities       |
| `lazyload.js`     | Lazy loading logic for OTOL subtrees              |
| `index.html`      | UI composition, module orchestration              |
| `style.css`       | Styles for visualization and UI                   |

---

## Data Flow

1. **Initial Load**:  
   - User selects dataset (sample or OTOL) in `index.html`.
   - The chosen JSON or OTOL-derived root is loaded and passed to `cladogram.js`.

2. **Rendering**:  
   - `cladogram.js` draws the tree using D3.js, attaches event listeners for expansion, tooltips, and search.

3. **Tooltip**:  
   - On node hover, `tooltip.js` formats and displays metadata, including name, rank, OTT ID, synonyms, and sources.

4. **Search**:  
   - `search.js` handles search input, highlights matching nodes, and reveals their ancestors.

5. **Lazy Loading**:  
   - On expanding an unloaded node with an `ott_id`, `lazyload.js` fetches `/subtree?ott_id=...` and merges children.
   - A loading spinner is displayed until data arrives.

---

## Extending

- To add more metadata fields:  
  1. Update the backend to parse and include them.
  2. Update `tooltip.js` to render them.

- To support new data sources:  
  1. Add a new loader in `lazyload.js`.
  2. Register the dataset in the dropdown in `index.html`.

---

## Module Documentation

### cladogram.js

- `renderCladogram(data, options)`:  
  Renders the tree, supports options for tooltips, lazy loading, etc.

### tooltip.js

- `showTooltip(event, d, selector)`:  
  Renders metadata-rich tooltips.
- `hideTooltip(selector)`:  
  Hides the tooltip.

### search.js

- `searchTree(node, term)`:  
  Recursively marks nodes that match the search term.
- `revealNode(node)`:  
  Expands ancestors for visibility.

### lazyload.js

- `fetchSubtree(ott_id, callback)`:  
  Calls backend `/subtree?ott_id=...`, returns children to callback.

---

## Reproducibility & Scientific Best Practices

- All modules are pure, stateless, and documented.
- Data provenance is preserved and displayed (see tooltips).
- Code is separated for easy review and extension.

---

## See Also

- [README.md](./README.md) — Project overview, backend flow, and scientific context.