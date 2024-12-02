import unittest
from datetime import datetime, timedelta
from src.utils.date_filter import filter_by_date
from src.paper import Paper

class TestDateFilter(unittest.TestCase):
    def test_filter_by_date(self):
        paper1 = Paper('cs.CL', 'Title1', 'Author1', 'Abstract1', (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ'), 'http://link1')
        paper2 = Paper('cs.CL', 'Title2', 'Author2', 'Abstract2', (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%dT%H:%M:%SZ'), 'http://link2')
        papers = [paper1, paper2]
        recent_papers = filter_by_date(papers, 7)
        self.assertEqual(len(recent_papers), 1)
        self.assertEqual(recent_papers[0].title, 'Title1')

if __name__ == '__main__':
    unittest.main()
