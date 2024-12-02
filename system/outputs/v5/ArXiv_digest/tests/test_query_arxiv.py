import unittest
from src.query_arxiv import QueryArXiv

class TestQueryArXiv(unittest.TestCase):
    def test_construct_query_url(self):
        query = QueryArXiv(category='cs.CL', title='neural', author='Smith', abstract='learning')
        url = query.construct_query_url()
        expected_url = "http://export.arxiv.org/api/query?search_query=cat:cs.CL+AND+ti:neural+AND+au:Smith+AND+abs:learning&sortBy=submittedDate&sortOrder=descending&start=0&max_results=10"
        self.assertEqual(url, expected_url)

    # Additional tests for execute_query, etc.

if __name__ == '__main__':
    unittest.main()
