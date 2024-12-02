import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from src.query_arxiv import QueryArXiv
from src.utils.api_interaction import APIInteraction
from src.utils.xml_parser import XMLParser
from src.utils.output_handler import OutputHandler
from src.utils.command_line_interface import CommandLineInterface

class TestQueryArXiv(unittest.TestCase):
    def test_construct_query_url(self):
        query = QueryArXiv(category='cs.CL', title='neural', author='Smith', abstract='learning', recent_days=30)
        url = query.constructQueryURL()
        self.assertIn('search_query=cat:cs.CL+AND+ti:neural+AND+au:Smith+AND+abs:learning', url)
        self.assertIn('sortBy=submittedDate', url)
        self.assertIn('sortOrder=descending', url)

    def test_filter_by_date(self):
        query = QueryArXiv(recent_days=30)
        data = [
            {'published': (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%dT%H:%M:%SZ')},
            {'published': (datetime.now() - timedelta(days=40)).strftime('%Y-%m-%dT%H:%M:%SZ')},
        ]
        filtered_data = query.filterByDate(data)
        self.assertEqual(len(filtered_data), 1)

    @patch.object(APIInteraction, 'fetchData')
    @patch.object(XMLParser, 'parseData')
    @patch.object(OutputHandler, 'printToConsole')
    @patch.object(OutputHandler, 'saveToCSV')
    def test_execute_query(self, mock_save_to_csv, mock_print_to_console, mock_parse_data, mock_fetch_data):
        mock_fetch_data.return_value = b'<xml>data</xml>'
        mock_parse_data.return_value = [
            {'category': 'cs.CL', 'title': 'Sample Title', 'author': 'Author Name', 'abstract': 'Sample abstract.',
             'published': (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%dT%H:%M:%SZ'),
             'link': 'http://arxiv.org/abs/1234.5678v1'}
        ]
        query = QueryArXiv(category='cs.CL', title='neural', author='Smith', abstract='learning', recent_days=30, verbose=True, to_file='results.csv')
        query.executeQuery()
        mock_fetch_data.assert_called_once()
        mock_parse_data.assert_called_once()
        mock_print_to_console.assert_called_once()
        mock_save_to_csv.assert_called_once()

class TestCommandLineInterface(unittest.TestCase):
    def test_parse_arguments(self):
        cli = CommandLineInterface()
        args = [
            '--category', 'cs.CL',
            '--title', 'neural',
            '--author', 'Smith',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--to_file', 'results.csv',
            '--verbose'
        ]
        parsed_args = cli.parse_arguments(args)
        self.assertEqual(parsed_args['category'], 'cs.CL')
        self.assertEqual(parsed_args['title'], 'neural')
        self.assertEqual(parsed_args['author'], 'Smith')
        self.assertEqual(parsed_args['abstract'], 'learning')
        self.assertEqual(parsed_args['recent_days'], 30)
        self.assertEqual(parsed_args['to_file'], 'results.csv')
        self.assertTrue(parsed_args['verbose'])

    def test_missing_required_argument(self):
        cli = CommandLineInterface()
        args = ['--category', 'cs.CL']
        with self.assertRaises(SystemExit):
            cli.parse_arguments(args)

if __name__ == '__main__':
    unittest.main()
