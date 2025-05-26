# Troubleshooting / FAQ

## Q: The tree fails to load or expand nodes. What should I do?
- **A:** Ensure the backend (`backend_service.py`) is running on `localhost:5001`.
- Make sure you have Python 3.8+ and required dependencies: `pip install flask flask-cors requests`
- Check your browser's console for CORS/network errors.
- If using a large tree, try with `otol_eukaryota_sample.json` first.

## Q: Expanding a node does not load children in the real OTOL tree.
- **A:** The backend may be down, or the OTOL API may be temporarily unavailable.
- Try reloading or check the backend logs for errors.

## Q: I want to use a different clade or subtree.
- **A:** Run in `scripts/`:  
    ```
    python fetch_otol_subtree.py --ott-id <YOUR_OTT_ID> --output ../web/your_tree.json
    ```
- Use the [Open Tree of Life browser](https://tree.opentreeoflife.org/) to find OTT IDs.

## Q: How can I extend tooltips or add new metadata?
- **A:** Update the backend parser (`phyloxml_parser.py`) to extract new fields.
- Update `tooltip.js` to display them.

## Q: Where is the data coming from?
- **A:** All real data is fetched from the [Open Tree of Life](https://tree.opentreeoflife.org/) API. Sample data is included for offline demo.

## Q: Can I deploy this remotely?
- **A:** Yes, but ensure the backend is publicly accessible and CORS is enabled. For production, deploy with a WSGI server (e.g., gunicorn).

---