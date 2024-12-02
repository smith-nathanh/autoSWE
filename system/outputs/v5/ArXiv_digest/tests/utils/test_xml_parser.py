import unittest
from src.utils.xml_parser import parse_xml_data

class TestXmlParser(unittest.TestCase):
    def test_parse_xml_data(self):
        xml_data = '''<feed xmlns="http://www.w3.org/2005/Atom">
            <entry>
                <title>Sample Title</title>
                <author><name>John Doe</name></author>
                <summary>Sample abstract</summary>
                <published>2023-10-01T12:00:00Z</published>
                <id>http://arxiv.org/abs/1234.5678</id>
                <primary_category xmlns="http://arxiv.org/schemas/atom" term="cs.CL"/>
            </entry>
        </feed>'''
        papers = parse_xml_data(xml_data)
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].title, 'Sample Title')

if __name__ == '__main__':
    unittest.main()
