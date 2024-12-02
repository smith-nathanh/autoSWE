import unittest
from unittest.mock import patch, MagicMock
from query_arxiv import QueryArXiv
from arxiv_api import ArXivAPI
from xml_parser import XMLParser
from csv_exporter import CSVExporter
from utils.date_utils import check_date
import datetime

class TestQueryArXiv(unittest.TestCase):
    def setUp(self):
        self.query = QueryArXiv(category='cs.CL', title='neural', author='Smith', abstract='learning', recent_days=7, verbose=True)

    @patch('arxiv_api.ArXivAPI.fetch_data')
    @patch('xml_parser.XMLParser.parse_xml')
    def test_execute_query(self, mock_parse_xml, mock_fetch_data):
        mock_fetch_data.return_value = '<xml></xml>'
        mock_parse_xml.return_value = [
            {
                'category': 'cs.CL',
                'title': 'Neural Networks',
                'author': 'John Smith',
                'abstract': 'Learning about neural networks.',
                'published': '2023-10-01T00:00:00Z',
                'link': 'http://arxiv.org/abs/1234.5678'
            }
        ]

        with patch('builtins.print') as mock_print:
            self.query.execute_query()
            mock_print.assert_called_with('Link: http://arxiv.org/abs/1234.5678')

    def test_filter_results_by_date(self):
        results = [
            {'published': '2023-10-01T00:00:00Z'},
            {'published': '2023-09-01T00:00:00Z'}
        ]
        filtered_results = self.query.filter_results_by_date(results)
        self.assertEqual(len(filtered_results), 1)

    @patch('csv_exporter.CSVExporter.export_to_csv')
    def test_output_results_to_file(self, mock_export_to_csv):
        self.query.to_file = 'output.csv'
        results = [
            {
                'category': 'cs.CL',
                'title': 'Neural Networks',
                'author': 'John Smith',
                'abstract': 'Learning about neural networks.',
                'published': '2023-10-01T00:00:00Z',
                'link': 'http://arxiv.org/abs/1234.5678'
            }
        ]
        self.query.output_results(results)
        mock_export_to_csv.assert_called_once_with(results, 'output.csv')

class TestArXivAPI(unittest.TestCase):
    def test_construct_query_url(self):
        api = ArXivAPI()
        url = api.construct_query_url('cs.CL', 'neural', 'Smith', 'learning', 10)
        expected_url = 'http://export.arxiv.org/api/query?search_query=cat:cs.CL+AND+ti:neural+AND+au:Smith+AND+abs:learning&sortBy=submittedDate&sortOrder=descending&start=0&max_results=10'
        self.assertEqual(url, expected_url)

class TestXMLParser(unittest.TestCase):
    def test_parse_xml(self):
        parser = XMLParser()
        xml_data = '''<feed xmlns="http://arxiv.org/schemas/atom">
            <entry>
                <primary_category term="cs.CL"/>
                <title>Neural Networks</title>
                <author><name>John Smith</name></author>
                <summary>Learning about neural networks.</summary>
                <published>2023-10-01T00:00:00Z</published>
                <id>http://arxiv.org/abs/1234.5678</id>
            </entry>
        </feed>'''
        results = parser.parse_xml(xml_data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'Neural Networks')

class TestCSVExporter(unittest.TestCase):
    @patch('csv.writer')
    def test_export_to_csv(self, mock_csv_writer):
        exporter = CSVExporter()
        results = [
            {
                'category': 'cs.CL',
                'title': 'Neural Networks',
                'author': 'John Smith',
                'abstract': 'Learning about neural networks.',
                'published': '2023-10-01T00:00:00Z',
                'link': 'http://arxiv.org/abs/1234.5678'
            }
        ]
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            exporter.export_to_csv(results, 'output.csv')
            mock_csv_writer().writerow.assert_any_call({'category': 'cs.CL', 'title': 'Neural Networks', 'author': 'John Smith', 'abstract': 'Learning about neural networks.', 'published': '2023-10-01T00:00:00Z', 'link': 'http://arxiv.org/abs/1234.5678'})

class TestDateUtils(unittest.TestCase):
    def test_check_date(self):
        self.assertTrue(check_date('2023-10-01T00:00:00Z', 7))
        self.assertFalse(check_date('2023-09-01T00:00:00Z', 7))

if __name__ == '__main__':
    unittest.main()
