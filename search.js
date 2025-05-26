// search.js - Tree of Life Cladogram project
// Modular search/match/reveal utilities

/**
 * Recursively search tree for nodes matching term.
 * Marks node.matched = true for matches, collects in matchedNodes.
 * @param {object} node - root node
 * @param {string} term - lowercase search term
 * @param {Array} matchedNodes - array to store matches (optional)
 */
export function searchTree(node, term, matchedNodes = []) {
  node.matched = false;
  if (node.name && node.name.toLowerCase().includes(term)) {
    node.matched = true;
    matchedNodes.push(node);
    revealNode(node);
  }
  if (node.children) node.children.forEach(child => searchTree(child, term, matchedNodes));
  if (node._children) node._children.forEach(child => searchTree(child, term, matchedNodes));
  return matchedNodes;
}

/**
 * Recursively expand ancestors so node is visible.
 * @param {object} node
 */
export function revealNode(node) {
  if (node.parent) {
    if (node.parent._children) {
      node.parent.children = node.parent._children;
      node.parent._children = null;
    }
    revealNode(node.parent);
  }
}

/**
 * Recursively clears .matched state from tree.
 * @param {object} node
 */
export function clearHighlights(node) {
  node.matched = false;
  if (node.children) node.children.forEach(clearHighlights);
  if (node._children) node._children.forEach(clearHighlights);
}