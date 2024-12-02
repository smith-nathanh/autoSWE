# tests/test_downloader.py

import unittest
from chakin.chakin import Chakin

class TestChakin(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin(csv_path='chakin/datasets.csv')

    def test_search(self):
        results = self.chakin.search(lang='Arabic')
        self.assertIn('fastText(ar)', results)

    def test_download(self):
        # This is a placeholder for the download test
        # You would typically mock network requests here
        pass

if __name__ == '__main__':
    unittest.main()
