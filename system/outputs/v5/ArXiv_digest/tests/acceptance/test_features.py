import unittest
from unittest.mock import patch, MagicMock
from src.query_arxiv import QueryArXiv
from src.utils.api_interaction import fetch_data
from src.utils.xml_parser import parse_xml_data
from src.utils.date_filter import filter_by_date
from src.utils.output_handler import output_results
from datetime import datetime, timedelta
import os

class TestQueryArXivFeatures(unittest.TestCase):
    def setUp(self):
        self.query = QueryArXiv(category='cs.CL', title='neural', author='Smith', abstract='learning', recent_days=7)
        self.mock_xml_data = '''<feed xmlns="http://www.w3.org/2005/Atom">
            <entry>
                <title>Sample Title</title>
                <author><name>John Doe</name></author>
                <summary>Sample abstract</summary>
                <published>2023-10-01T12:00:00Z</published>
                <id>http://arxiv.org/abs/1234.5678</id>
                <primary_category xmlns="http://arxiv.org/schemas/atom" term="cs.CL"/>
            </entry>
        </feed>'''

    @patch('src.utils.api_interaction.urllib.request.urlopen')
    def test_successful_query_execution(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = self.mock_xml_data
        self.query.execute_query()
        # Assuming output_results is patched to verify its call

    def test_construct_query_url(self):
        expected_url = "http://export.arxiv.org/api/query?search_query=cat:cs.CL+AND+ti:neural+AND+au:Smith+AND+abs:learning&sortBy=submittedDate&sortOrder=descending&start=0&max_results=10"
        self.assertEqual(self.query.construct_query_url(), expected_url)

    def test_filter_by_recent_days(self):
        papers = parse_xml_data(self.mock_xml_data)
        recent_papers = filter_by_date(papers, 7)
        self.assertEqual(len(recent_papers), 1)

    def test_output_results_to_console(self):
        papers = parse_xml_data(self.mock_xml_data)
        with patch('builtins.print') as mocked_print:
            output_results(papers, None, True)
            mocked_print.assert_called()  # Check if print was called

    def test_output_results_to_file(self):
        papers = parse_xml_data(self.mock_xml_data)
        test_file = 'test_output.csv'
        output_results(papers, test_file, False)
        self.assertTrue(os.path.exists(test_file))
        os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
