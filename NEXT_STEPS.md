# Next Steps: Tree of Life Cladogram Project

## 1. Modularization and Documentation

- **Objective:** Ensure all code is logically separated, reusable, and well-documented for scientific and technical users.
- **Actions:**
  - Split backend (Python) into modules: API handler, OTOL fetcher, phyloXML parser.
  - Split frontend (JS) into modules: core rendering, tooltip logic, lazy loading logic.
  - Add docstrings, JSDoc, and function-level comments.
  - Document each endpoint, function, and data structure in the code and README.

## 2. Metadata Enrichment & Display

- **Objective:** Make the tooltips and node popups maximally informative for biologists and developers.
- **Actions:**
  - Add support in the backend and frontend for new metadata fields when present (e.g., full taxonomy path, NCBI/GBIF links, publication references).
  - Clearly display all sources and URIs as clickable links.
  - Document how to extend the parser and tooltip for additional metadata.

## 3. Enhanced Error Handling & User Feedback

- **Objective:** Ensure robust operation and clear user communication.
- **Actions:**
  - Display clear error or warning messages in the web app if a fetch or parse fails.
  - Log backend errors with context and guidance for debugging.

## 4. Workflow & Data Flow Documentation

- **Objective:** Enable users and contributors to understand, reproduce, and extend the workflow.
- **Actions:**
  - Add a section to README and/or a dedicated `WORKFLOW.md` explaining:
    - Data flow from API call to web visualization
    - How nodes and subtrees are fetched, parsed, merged, and displayed
    - How to add support for a new field or metadata

---

## Immediate Next Task

**Refactor the backend Python service into modular components, and update the README with a section documenting the backend modules and workflow.**