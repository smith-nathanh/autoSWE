import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from src.query_arxiv import QueryArXiv
from src.paper import Paper
from src.utils.api_interaction import fetch_data
from src.utils.xml_parser import parse_xml_data
from src.utils.date_filter import filter_by_date
from src.utils.output_handler import output_results
import os

class TestQueryArXiv(unittest.TestCase):
    def test_construct_query_url(self):
        query = QueryArXiv(category='cs.CL', title='neural', author='Smith', abstract='learning')
        url = query.construct_query_url()
        expected_url = "http://export.arxiv.org/api/query?search_query=cat:cs.CL+AND+ti:neural+AND+au:Smith+AND+abs:learning&sortBy=submittedDate&sortOrder=descending&start=0&max_results=10"
        self.assertEqual(url, expected_url)

    def test_execute_query_no_params(self):
        with self.assertRaises(SystemExit):
            query = QueryArXiv()
            query.execute_query()

    @patch('src.utils.api_interaction.fetch_data')
    @patch('src.utils.xml_parser.parse_xml_data')
    @patch('src.utils.date_filter.filter_by_date')
    @patch('src.utils.output_handler.output_results')
    def test_execute_query(self, mock_output, mock_filter, mock_parse, mock_fetch):
        mock_fetch.return_value = b'<xml>data</xml>'
        mock_parse.return_value = [Paper('cs.CL', 'Title', 'Author', 'Abstract', '2023-10-01T12:00:00Z', 'http://link')]
        mock_filter.return_value = mock_parse.return_value
        query = QueryArXiv(category='cs.CL', recent_days=7, verbose=True)
        query.execute_query()
        mock_output.assert_called_once()

class TestPaper(unittest.TestCase):
    def test_paper_initialization(self):
        paper = Paper('cs.CL', 'Sample Title', 'John Doe', 'Sample abstract', '2023-10-01T12:00:00Z', 'http://arxiv.org/abs/1234.5678')
        self.assertEqual(paper.category, 'cs.CL')
        self.assertEqual(paper.title, 'Sample Title')
        self.assertEqual(paper.author, 'John Doe')
        self.assertEqual(paper.abstract, 'Sample abstract')
        self.assertEqual(paper.published, datetime(2023, 10, 1, 12, 0, 0))
        self.assertEqual(paper.link, 'http://arxiv.org/abs/1234.5678')

class TestApiInteraction(unittest.TestCase):
    @patch('src.utils.api_interaction.urllib.request.urlopen')
    def test_fetch_data(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = b'<xml>data</xml>'
        result = fetch_data('http://example.com')
        self.assertEqual(result, b'<xml>data</xml>')

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

class TestDateFilter(unittest.TestCase):
    def test_filter_by_date(self):
        paper1 = Paper('cs.CL', 'Title1', 'Author1', 'Abstract1', (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ'), 'http://link1')
        paper2 = Paper('cs.CL', 'Title2', 'Author2', 'Abstract2', (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%dT%H:%M:%SZ'), 'http://link2')
        papers = [paper1, paper2]
        recent_papers = filter_by_date(papers, 7)
        self.assertEqual(len(recent_papers), 1)
        self.assertEqual(recent_papers[0].title, 'Title1')

class TestOutputHandler(unittest.TestCase):
    def setUp(self):
        self.papers = [
            Paper('cs.CL', 'Title1', 'Author1', 'Abstract1', '2023-10-01T12:00:00Z', 'http://link1'),
            Paper('cs.CL', 'Title2', 'Author2', 'Abstract2', '2023-10-02T12:00:00Z', 'http://link2')
        ]
        self.test_file = 'test_output.csv'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_output_results_to_file(self):
        output_results(self.papers, self.test_file, False)
        self.assertTrue(os.path.exists(self.test_file))

    def test_output_results_verbose(self):
        with patch('builtins.print') as mocked_print:
            output_results(self.papers, None, True)
            self.assertEqual(mocked_print.call_count, 12)  # 6 lines per paper, 2 papers

if __name__ == '__main__':
    unittest.main()
