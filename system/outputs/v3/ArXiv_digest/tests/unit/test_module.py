import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
import sys
import os

# Adjust the path to import the modules correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from query_arxiv import QueryArXiv
from utils.xml_parser import XMLParser
from utils.csv_exporter import CSVExporter
from api.arxiv_api import ArXivAPI

class TestQueryArXiv(unittest.TestCase):
    def setUp(self):
        self.query_arxiv = QueryArXiv()

    def test_argument_parsing(self):
        test_args = [
            'query_arxiv.py', '--category', 'cs.CL', '--title', 'neural', '--author', 'Smith', '--abstract', 'learning', '--recent_days', '7'
        ]
        with patch.object(sys, 'argv', test_args):
            self.query_arxiv._parse_arguments()
            self.assertEqual(self.query_arxiv.category, 'cs.CL')
            self.assertEqual(self.query_arxiv.title, 'neural')
            self.assertEqual(self.query_arxiv.author, 'Smith')
            self.assertEqual(self.query_arxiv.abstract, 'learning')
            self.assertEqual(self.query_arxiv.recent_days, 7)

    def test_argument_validation(self):
        test_args = [
            'query_arxiv.py', '--category', 'cs.CL', '--title', 'neural', '--author', 'Smith', '--abstract', 'learning', '--recent_days', '7'
        ]
        with patch.object(sys, 'argv', test_args):
            self.query_arxiv._parse_arguments()
            # Valid arguments should not raise an error
            self.query_arxiv._validate_arguments()

        invalid_args = [
            'query_arxiv.py', '--category', 'cs.CL', '--title', 'neural!', '--author', 'Smith', '--abstract', 'learning', '--recent_days', '7'
        ]
        with patch.object(sys, 'argv', invalid_args):
            self.query_arxiv._parse_arguments()
            with self.assertRaises(ValueError):
                self.query_arxiv._validate_arguments()

    def test_construct_query_url(self):
        self.query_arxiv.category = 'cs.CL'
        self.query_arxiv.title = 'neural'
        self.query_arxiv.author = 'Smith'
        self.query_arxiv.abstract = 'learning'
        expected_url = (
            "http://export.arxiv.org/api/query?search_query=cat:cs.CL+AND+ti:neural+AND+au:Smith+AND+abs:learning"
            "&sortBy=submittedDate&sortOrder=descending&start=0&max_results=10"
        )
        self.assertEqual(self.query_arxiv.construct_query_url(), expected_url)

    def test_check_date(self):
        self.query_arxiv.recent_days = 7
        recent_date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%dT%H:%M:%SZ')
        old_date = (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.assertTrue(self.query_arxiv.check_date(recent_date))
        self.assertFalse(self.query_arxiv.check_date(old_date))

class TestXMLParser(unittest.TestCase):
    def setUp(self):
        self.parser = XMLParser()

    def test_parse(self):
        xml_data = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
            <entry>
                <category term="cs.CL"/>
                <title>Neural Networks</title>
                <author><name>John Smith</name></author>
                <summary>Learning in neural networks</summary>
                <published>2023-10-01T00:00:00Z</published>
                <link href="http://arxiv.org/abs/1234.5678v1"/>
            </entry>
        </feed>
        '''
        results = self.parser.parse(xml_data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['category'], 'cs.CL')
        self.assertEqual(results[0]['title'], 'Neural Networks')
        self.assertEqual(results[0]['author'], 'John Smith')
        self.assertEqual(results[0]['abstract'], 'Learning in neural networks')
        self.assertEqual(results[0]['published'], '2023-10-01T00:00:00Z')
        self.assertEqual(results[0]['link'], 'http://arxiv.org/abs/1234.5678v1')

class TestCSVExporter(unittest.TestCase):
    def setUp(self):
        self.exporter = CSVExporter()

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_export_to_csv(self, mock_open):
        data = [
            {
                'category': 'cs.CL',
                'title': 'Neural Networks',
                'author': 'John Smith',
                'abstract': 'Learning in neural networks',
                'published': '2023-10-01T00:00:00Z',
                'link': 'http://arxiv.org/abs/1234.5678v1'
            }
        ]
        self.exporter.export_to_csv(data, 'dummy_path.csv')
        mock_open.assert_called_once_with('dummy_path.csv', mode='w', newline='', encoding='utf-8')
        handle = mock_open()
        handle.write.assert_any_call('category,title,author,abstract,published,link\n')
        handle.write.assert_any_call('cs.CL,Neural Networks,John Smith,Learning in neural networks,2023-10-01T00:00:00Z,http://arxiv.org/abs/1234.5678v1\n')

class TestArXivAPI(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_fetch_data(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'<xml>data</xml>'
        mock_urlopen.return_value = mock_response

        api = ArXivAPI()
        data = api.fetch_data('http://example.com')
        self.assertEqual(data, '<xml>data</xml>')
        mock_urlopen.assert_called_once_with('http://example.com')

if __name__ == '__main__':
    unittest.main()
