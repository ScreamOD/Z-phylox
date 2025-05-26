import json

# Enhanced sample with taxonomic ranks for better tooltips and extensibility
tree = {
    "name": "Eukaryota",
    "rank": "Domain",
    "children": [
        {
            "name": "Opisthokonta",
            "rank": "Supergroup",
            "children": [
                {
                    "name": "Metazoa (Animals)",
                    "rank": "Kingdom",
                    "children": [
                        {
                            "name": "Chordata",
                            "rank": "Phylum",
                            "children": [
                                {"name": "Mammalia", "rank": "Class", "children": [
                                    {"name": "Primates", "rank": "Order", "children": [
                                        {"name": "Hominidae", "rank": "Family", "children": [
                                            {"name": "Homo", "rank": "Genus", "children": [
                                                {"name": "Homo sapiens", "rank": "Species", "children": []}
                                            ]}
                                        ]}
                                    ]}
                                ]},
                                {"name": "Aves", "rank": "Class", "children": []},
                                {"name": "Actinopterygii", "rank": "Class", "children": []}
                            ]
                        },
                        {"name": "Arthropoda", "rank": "Phylum", "children": [
                            {"name": "Insecta", "rank": "Class", "children": []},
                            {"name": "Arachnida", "rank": "Class", "children": []}
                        ]}
                    ]
                },
                {"name": "Fungi", "rank": "Kingdom", "children": [
                    {"name": "Ascomycota", "rank": "Phylum", "children": []},
                    {"name": "Basidiomycota", "rank": "Phylum", "children": []}
                ]}
            ]
        },
        {
            "name": "Archaeplastida",
            "rank": "Supergroup",
            "children": [
                {"name": "Viridiplantae (Green plants)", "rank": "Kingdom", "children": [
                    {"name": "Bryophyta", "rank": "Phylum", "children": []},
                    {"name": "Tracheophyta", "rank": "Phylum", "children": [
                        {"name": "Magnoliopsida", "rank": "Class", "children": []},
                        {"name": "Pinopsida", "rank": "Class", "children": []}
                    ]}
                ]}
            ]
        },
        {
            "name": "SAR (Stramenopiles, Alveolates, Rhizaria)",
            "rank": "Supergroup",
            "children": [
                {"name": "Stramenopiles", "rank": "Group", "children": [
                    {"name": "Bacillariophyta (Diatoms)", "rank": "Phylum", "children": []}
                ]},
                {"name": "Alveolates", "rank": "Group", "children": [
                    {"name": "Dinoflagellata", "rank": "Phylum", "children": []}
                ]}
            ]
        }
    ]
}

with open("../web/otol_eukaryota_sample.json", "w") as f:
    json.dump(tree, f, indent=2)