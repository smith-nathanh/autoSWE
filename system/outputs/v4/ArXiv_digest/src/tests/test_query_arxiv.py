import unittest
from src.query_arxiv import QueryArXiv

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
            {'published': '2023-10-01T00:00:00Z'},
            {'published': '2023-09-01T00:00:00Z'},
        ]
        filtered_data = query.filterByDate(data)
        self.assertEqual(len(filtered_data), 1)
        self.assertEqual(filtered_data[0]['published'], '2023-10-01T00:00:00Z')

if __name__ == '__main__':
    unittest.main()
