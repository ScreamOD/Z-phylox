"""
Module: backend_service.py
==========================

Flask-based API service for the Tree of Life Cladogram project.
- Exposes /subtree?ott_id=ID to fetch and parse OTOL subtrees.
- Modular: Relies on otol_api.py and phyloxml_parser.py.

Author: Tree of Life Cladogram Project Contributors
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from otol_api import fetch_subtree
from phyloxml_parser import parse_phyloxml
import traceback
import logging

app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ToLBackend")

@app.route("/subtree", methods=["GET"])
def subtree_endpoint():
    ott_id = request.args.get("ott_id", type=int)
    if not ott_id:
        return jsonify({"error": "Missing ott_id parameter"}), 400
    try:
        xml_str = fetch_subtree(ott_id)
        tree = parse_phyloxml(xml_str)
        return jsonify(tree)
    except Exception as e:
        logger.error(f"Error fetching/parsing subtree for ott_id={ott_id}: {e}")
        logger.debug(traceback.format_exc())
        return jsonify({"error": f"{type(e).__name__}: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)