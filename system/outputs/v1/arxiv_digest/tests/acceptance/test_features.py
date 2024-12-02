import unittest
from unittest.mock import patch, MagicMock
from query_arxiv import QueryArXiv
import os

class TestQueryArXivFeatures(unittest.TestCase):
    def setUp(self):
        self.category = "cs.CL"
        self.title = "neural"
        self.author = "Smith"
        self.abstract = "learning"
        self.recent_days = 7
        self.max_results = 10
        self.verbose = True
        self.to_file = "test_output.csv"

    @patch('arxiv_api.ArXivAPI.fetch_data')
    @patch('xml_parser.XMLParser.parse_xml')
    def test_successful_query_execution(self, mock_parse_xml, mock_fetch_data):
        # Mocking API response
        mock_fetch_data.return_value = "<mocked_xml_data>"
        mock_parse_xml.return_value = [
            {
                'category': 'cs.CL',
                'title': 'Neural Networks for Learning',
                'author': 'John Smith',
                'abstract': 'This paper discusses neural networks.',
                'published': '2023-10-01T00:00:00Z',
                'link': 'http://arxiv.org/abs/1234.5678'
            }
        ]

        query = QueryArXiv(
            category=self.category,
            title=self.title,
            author=self.author,
            abstract=self.abstract,
            recent_days=self.recent_days,
            max_results=self.max_results,
            verbose=self.verbose,
            to_file=self.to_file
        )

        with patch('builtins.print') as mocked_print:
            query.execute_query()

            # Check console output
            mocked_print.assert_any_call('Category: cs.CL')
            mocked_print.assert_any_call('Title: Neural Networks for Learning')
            mocked_print.assert_any_call('Author: John Smith')
            mocked_print.assert_any_call('Abstract: This paper discusses neural networks.')
            mocked_print.assert_any_call('Published: 2023-10-01T00:00:00Z')
            mocked_print.assert_any_call('Link: http://arxiv.org/abs/1234.5678')

        # Check CSV output
        self.assertTrue(os.path.exists(self.to_file))
        with open(self.to_file, 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertIn('cs.CL', content)
            self.assertIn('Neural Networks for Learning', content)
            self.assertIn('John Smith', content)
            self.assertIn('This paper discusses neural networks.', content)
            self.assertIn('2023-10-01T00:00:00Z', content)
            self.assertIn('http://arxiv.org/abs/1234.5678', content)

        # Clean up
        os.remove(self.to_file)

    def test_invalid_query_parameters(self):
        with self.assertRaises(ValueError):
            QueryArXiv(
                category=None,
                title=None,
                author=None,
                abstract=None,
                recent_days=self.recent_days
            )

    @patch('utils.date_utils.check_date')
    def test_date_filtering(self, mock_check_date):
        mock_check_date.return_value = True

        query = QueryArXiv(
            category=self.category,
            title=self.title,
            author=self.author,
            abstract=self.abstract,
            recent_days=self.recent_days,
            max_results=self.max_results,
            verbose=self.verbose
        )

        with patch('xml_parser.XMLParser.parse_xml') as mock_parse_xml:
            mock_parse_xml.return_value = [
                {
                    'category': 'cs.CL',
                    'title': 'Neural Networks for Learning',
                    'author': 'John Smith',
                    'abstract': 'This paper discusses neural networks.',
                    'published': '2023-10-01T00:00:00Z',
                    'link': 'http://arxiv.org/abs/1234.5678'
                }
            ]

            results = query.filter_results_by_date(mock_parse_xml.return_value)
            self.assertEqual(len(results), 1)

if __name__ == '__main__':
    unittest.main()
