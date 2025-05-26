// index.js - Application entry point for Tree of Life Cladogram
import { renderCladogram } from './cladogram.js';
import { showTooltip, hideTooltip } from './tooltip.js';
import { searchTree, clearHighlights } from './search.js';
import { fetchSubtree } from './lazyload.js';

let treeData, currentDataset = "otol_eukaryota_sample.json";
let width = 1200, height = 800;

function loadAndRender(dataset) {
  fetch(dataset)
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        document.getElementById("tree").innerText =
          "Error loading tree data (" + dataset + "): " + data.error;
      } else {
        treeData = data;
        render(treeData);
      }
    })
    .catch((err) => {
      document.getElementById("tree").innerText =
        "Failed to load tree data (" + dataset + "). Please generate it or choose another dataset.";
    });
}

// ... (rest unchanged)