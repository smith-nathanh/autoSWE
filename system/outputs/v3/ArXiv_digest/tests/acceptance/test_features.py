import unittest
from unittest.mock import patch, MagicMock
import datetime
from src.query_arxiv import QueryArXiv

class TestQueryArXivFeatures(unittest.TestCase):
    def setUp(self):
        self.query_arxiv = QueryArXiv()

    @patch('src.api.arxiv_api.ArXivAPI.fetch_data')
    def test_successful_query_execution(self, mock_fetch_data):
        # Mock API response
        mock_fetch_data.return_value = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
            <entry>
                <category term="cs.CL"/>
                <title>Neural Networks</title>
                <author><name>John Smith</name></author>
                <summary>Learning in neural networks.</summary>
                <published>2023-10-01T00:00:00Z</published>
                <link href="http://arxiv.org/abs/1234.5678v1"/>
            </entry>
        </feed>
        '''

        # Set arguments
        self.query_arxiv.category = 'cs.CL'
        self.query_arxiv.title = 'Neural'
        self.query_arxiv.author = 'Smith'
        self.query_arxiv.abstract = 'Learning'
        self.query_arxiv.recent_days = 7
        self.query_arxiv.verbose = True

        # Capture output
        with patch('sys.stdout', new_callable=MagicMock()) as mock_stdout:
            self.query_arxiv.execute_query()
            output = mock_stdout.write.call_args_list

        # Check output
        self.assertIn('Category: cs.CL', str(output))
        self.assertIn('Title: Neural Networks', str(output))
        self.assertIn('Author: John Smith', str(output))
        self.assertIn('Abstract: Learning in neural networks.', str(output))
        self.assertIn('Published: 2023-10-01T00:00:00Z', str(output))
        self.assertIn('Link: http://arxiv.org/abs/1234.5678v1', str(output))

    def test_argument_validation(self):
        with self.assertRaises(ValueError):
            self.query_arxiv._validate_arguments()

        self.query_arxiv.category = 'cs.CL'
        self.query_arxiv._validate_arguments()  # Should not raise

    def test_date_check(self):
        self.query_arxiv.recent_days = 7
        valid_date = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime('%Y-%m-%dT%H:%M:%SZ')
        invalid_date = (datetime.datetime.now() - datetime.timedelta(days=10)).strftime('%Y-%m-%dT%H:%M:%SZ')

        self.assertTrue(self.query_arxiv.check_date(valid_date))
        self.assertFalse(self.query_arxiv.check_date(invalid_date))

if __name__ == '__main__':
    unittest.main()
