import unittest
from datetime import datetime
from src.paper import Paper

class TestPaper(unittest.TestCase):
    def test_paper_initialization(self):
        paper = Paper('cs.CL', 'Sample Title', 'John Doe', 'Sample abstract', '2023-10-01T12:00:00Z', 'http://arxiv.org/abs/1234.5678')
        self.assertEqual(paper.category, 'cs.CL')
        self.assertEqual(paper.title, 'Sample Title')
        self.assertEqual(paper.author, 'John Doe')
        self.assertEqual(paper.abstract, 'Sample abstract')
        self.assertEqual(paper.published, datetime(2023, 10, 1, 12, 0, 0))
        self.assertEqual(paper.link, 'http://arxiv.org/abs/1234.5678')

if __name__ == '__main__':
    unittest.main()
