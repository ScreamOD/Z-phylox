"""
Backend subtree fetcher: Given an OTT ID, return a subtree in the required JSON format,
including synonyms and source references if available.

For lazy loading in the frontend, this script can be wrapped in a minimal Flask API.

Example API usage:
GET /subtree?ott_id=9606

References:
  - https://github.com/OpenTreeOfLife/germinator/wiki/Open-Tree-of-Life-Web-APIs
  - http://www.phyloxml.org/documentation/version_1.10/phyloxml.xsd
"""

import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OTOL_API_URL = "https://api.opentreeoflife.org/v3/tree_of_life/subtree"

def fetch_subtree(ott_id):
    payload = {"ott_id": ott_id, "format": "phyloxml"}
    resp = requests.post(OTOL_API_URL, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.text

def parse_phyloxml(xml_str):
    """
    Parse phyloXML string and return a dict with:
      - name
      - ott_id
      - rank
      - synonyms (list of strings, if present)
      - sources (list of strings, if present)
      - children (recursive)
    """
    import xml.etree.ElementTree as ET
    ns = {'p': 'http://www.phyloxml.org'}
    root = ET.fromstring(xml_str)

    def parse_clade(clade):
        name = clade.find('p:name', ns)
        tax = clade.find('p:taxonomy', ns)
        taxid, rank, synonyms, sources = None, None, [], []
        if tax is not None:
            taxid_elem = tax.find('p:id', ns)
            if taxid_elem is not None:
                taxid = taxid_elem.text
            r = tax.find('p:rank', ns)
            if r is not None:
                rank = r.text
            # Synonyms: <synonym>
            for syn in tax.findall('p:synonym', ns):
                if syn.text:
                    synonyms.append(syn.text)
            # Sources: <uri> or <code>
            for src in tax.findall('p:uri', ns):
                if src.text:
                    sources.append(src.text)
            for src in tax.findall('p:code', ns):
                if src.text:
                    sources.append(src.text)
        ott_id = None
        if taxid and taxid.startswith("ott"):
            ott_id = int(taxid.replace("ott", ""))
        node = {
            "name": name.text if name is not None else "",
            "children": [parse_clade(c) for c in clade.findall('p:clade', ns)],
        }
        if ott_id: node["ott_id"] = ott_id
        if rank: node["rank"] = rank
        if synonyms: node["synonyms"] = synonyms
        if sources: node["sources"] = sources
        return node

    clade = root.find('.//p:clade', ns)
    if clade is None:
        raise ValueError("No clade found in phyloxml.")
    return parse_clade(clade)

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
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)