"""
Module: phyloxml_parser.py
==========================

Parses phyloXML strings into a hierarchical dict suitable for D3.js visualization, 
including fields: name, ott_id, rank, synonyms, sources, children, taxonomy_path, external_ids.

Functions:
    - parse_phyloxml(xml_str: str) -> dict

Author: Tree of Life Cladogram Project Contributors
"""

import xml.etree.ElementTree as ET

def parse_phyloxml(xml_str):
    """
    Parse a phyloXML string and return the corresponding tree as a dict.

    Args:
        xml_str (str): phyloXML-formatted string.

    Returns:
        dict: Node with 'name', 'ott_id', 'rank', 'synonyms', 'sources', 'children', 'taxonomy_path', 'external_ids'.
    """
    ns = {'p': 'http://www.phyloxml.org'}
    root = ET.fromstring(xml_str)

    def parse_clade(clade, path=None):
        name = clade.find('p:name', ns)
        tax = clade.find('p:taxonomy', ns)
        taxid, rank, synonyms, sources, external_ids = None, None, [], [], {}
        if tax is not None:
            taxid_elem = tax.find('p:id', ns)
            if taxid_elem is not None:
                taxid = taxid_elem.text
            r = tax.find('p:rank', ns)
            if r is not None:
                rank = r.text
            for syn in tax.findall('p:synonym', ns):
                if syn.text:
                    synonyms.append(syn.text)
            for src in tax.findall('p:uri', ns):
                if src.text:
                    sources.append(src.text)
            for src in tax.findall('p:code', ns):
                if src.text:
                    sources.append(src.text)
            for ext in tax.findall('p:db_reference', ns):
                db = ext.attrib.get('type')
                val = ext.attrib.get('id')
                if db and val:
                    external_ids[db] = val
        ott_id = None
        if taxid and taxid.startswith("ott"):
            ott_id = int(taxid.replace("ott", ""))
        node_name = name.text if name is not None else ""
        # Taxonomy path as a list of names
        path = (path or []) + [node_name]
        node = {
            "name": node_name,
            "children": [parse_clade(c, path) for c in clade.findall('p:clade', ns)],
            "taxonomy_path": path,
        }
        if ott_id: node["ott_id"] = ott_id
        if rank: node["rank"] = rank
        if synonyms: node["synonyms"] = synonyms
        if sources: node["sources"] = sources
        if external_ids: node["external_ids"] = external_ids
        return node

    clade = root.find('.//p:clade', ns)
    if clade is None:
        raise ValueError("No clade found in phyloxml.")
    return parse_clade(clade)