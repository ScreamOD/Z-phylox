"""
Basic test for phyloxml_parser.py
"""
import unittest
from phyloxml_parser import parse_phyloxml

SAMPLE_PHYLOXML = """<?xml version="1.0" encoding="UTF-8"?>
<phyloxml xmlns="http://www.phyloxml.org">
  <phylogeny rooted="true">
    <clade>
      <name>Eukaryota</name>
      <taxonomy>
        <id provider="ott">ott2759</id>
        <rank>domain</rank>
      </taxonomy>
      <clade>
        <name>Opisthokonta</name>
        <taxonomy>
          <id provider="ott">ott331920</id>
          <rank>supergroup</rank>
        </taxonomy>
      </clade>
    </clade>
  </phylogeny>
</phyloxml>
"""

class TestPhyloxmlParser(unittest.TestCase):
    def test_simple_tree(self):
        out = parse_phyloxml(SAMPLE_PHYLOXML)
        self.assertEqual(out['name'], 'Eukaryota')
        self.assertEqual(out['children'][0]['name'], 'Opisthokonta')
        self.assertEqual(out['children'][0]['rank'], 'supergroup')

if __name__ == '__main__':
    unittest.main()