import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from src.query_arxiv import QueryArXiv
from src.arxiv_api import ArXivAPI
from src.xml_parser import XMLParser
from src.csv_exporter import CSVExporter

class TestQueryArXiv(unittest.TestCase):
    def setUp(self):
        self.args = [
            '--category', 'cs.CL',
            '--author', 'Smith',
            '--title', 'neural',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--to_file', 'test.csv',
            '--verbose'
        ]
        self.query_arxiv = QueryArXiv(self.args)

    def test_parse_arguments(self):
        args = self.query_arxiv.parse_arguments(self.args)
        self.assertEqual(args.category, 'cs.CL')
        self.assertEqual(args.author, 'Smith')
        self.assertEqual(args.title, 'neural')
        self.assertEqual(args.abstract, 'learning')
        self.assertEqual(args.recent_days, 30)
        self.assertEqual(args.to_file, 'test.csv')
        self.assertTrue(args.verbose)

    @patch.object(ArXivAPI, 'fetch_data')
    @patch.object(XMLParser, 'parse')
    def test_execute_query(self, mock_parse, mock_fetch_data):
        mock_fetch_data.return_value = '<xml></xml>'
        mock_parse.return_value = [
            {
                'category': 'cs.CL',
                'title': 'Neural Networks for NLP',
                'author': 'John Smith',
                'abstract': 'This paper explores...',
                'published': (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                'link': 'http://arxiv.org/abs/1234.5678'
            }
        ]
        with patch.object(self.query_arxiv, 'output_results') as mock_output_results:
            with patch.object(CSVExporter, 'export_to_csv') as mock_export_to_csv:
                self.query_arxiv.execute_query()
                mock_output_results.assert_called_once()
                mock_export_to_csv.assert_called_once()

    def test_construct_query_url(self):
        expected_url = (
            "http://export.arxiv.org/api/query?"
            "search_query=cat:cs.CL+AND+au:Smith+AND+ti:neural+AND+abs:learning"
            "&sortBy=submittedDate&sortOrder=descending&start=0&max_results=10"
        )
        self.assertEqual(self.query_arxiv.construct_query_url(), expected_url)

    def test_check_date(self):
        recent_date = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
        old_date = (datetime.now() - timedelta(days=40)).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.assertTrue(self.query_arxiv.check_date(recent_date))
        self.assertFalse(self.query_arxiv.check_date(old_date))

class TestXMLParser(unittest.TestCase):
    def test_parse(self):
        xml_data = '''<feed xmlns:arxiv="http://arxiv.org/schemas/atom">
            <arxiv:entry>
                <arxiv:category term="cs.CL"/>
                <arxiv:title>Neural Networks for NLP</arxiv:title>
                <arxiv:author><arxiv:name>John Smith</arxiv:name></arxiv:author>
                <arxiv:summary>This paper explores...</arxiv:summary>
                <arxiv:published>2023-10-01T00:00:00Z</arxiv:published>
                <arxiv:link href="http://arxiv.org/abs/1234.5678"/>
            </arxiv:entry>
        </feed>'''
        parser = XMLParser()
        results = parser.parse(xml_data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['category'], 'cs.CL')
        self.assertEqual(results[0]['title'], 'Neural Networks for NLP')
        self.assertEqual(results[0]['author'], 'John Smith')
        self.assertEqual(results[0]['abstract'], 'This paper explores...')
        self.assertEqual(results[0]['published'], '2023-10-01T00:00:00Z')
        self.assertEqual(results[0]['link'], 'http://arxiv.org/abs/1234.5678')

class TestCSVExporter(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_export_to_csv(self, mock_open):
        data = [
            {
                'category': 'cs.CL',
                'title': 'Neural Networks for NLP',
                'author': 'John Smith',
                'abstract': 'This paper explores...',
                'published': '2023-10-01T00:00:00Z',
                'link': 'http://arxiv.org/abs/1234.5678'
            }
        ]
        exporter = CSVExporter()
        exporter.export_to_csv(data, 'test.csv')
        mock_open.assert_called_once_with('test.csv', mode='w', newline='', encoding='utf-8')
        handle = mock_open()
        handle.write.assert_any_call('category,title,author,abstract,published,link\n')
        handle.write.assert_any_call('cs.CL,Neural Networks for NLP,John Smith,This paper explores...,2023-10-01T00:00:00Z,http://arxiv.org/abs/1234.5678\n')

if __name__ == '__main__':
    unittest.main()
