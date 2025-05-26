"""
Module: otol_api.py
===================

Handles communication with the Open Tree of Life (OTOL) API.

Functions:
    - fetch_subtree(ott_id: int) -> str: 
        Fetches the phyloXML subtree for a given OTT ID from OTOL.

Author: Tree of Life Cladogram Project Contributors
"""

import requests

OTOL_API_URL = "https://api.opentreeoflife.org/v3/tree_of_life/subtree"

def fetch_subtree(ott_id):
    """
    Fetch the subtree for a given OTT ID from OTOL's API in phyloXML format.

    Args:
        ott_id (int): OTT ID of the desired clade root.

    Returns:
        str: phyloXML string.

    Raises:
        requests.RequestException: If the network request fails.
    """
    payload = {"ott_id": ott_id, "format": "phyloxml"}
    resp = requests.post(OTOL_API_URL, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.text