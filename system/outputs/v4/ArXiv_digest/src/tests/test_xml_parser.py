import unittest
from src.utils.xml_parser import XMLParser

class TestXMLParser(unittest.TestCase):
    def test_parse_data(self):
        xml_data = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
            <entry>
                <category term="cs.CL"/>
                <title>Sample Title</title>
                <author><name>Author Name</name></author>
                <summary>Sample abstract.</summary>
                <published>2023-10-01T00:00:00Z</published>
                <link href="http://arxiv.org/abs/1234.5678v1"/>
            </entry>
        </feed>
        '''
        parser = XMLParser()
        data = parser.parseData(xml_data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['category'], 'cs.CL')
        self.assertEqual(data[0]['title'], 'Sample Title')
        self.assertEqual(data[0]['author'], 'Author Name')
        self.assertEqual(data[0]['abstract'], 'Sample abstract.')
        self.assertEqual(data[0]['published'], '2023-10-01T00:00:00Z')
        self.assertEqual(data[0]['link'], 'http://arxiv.org/abs/1234.5678v1')

if __name__ == '__main__':
    unittest.main()
