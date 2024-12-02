import unittest
from unittest.mock import patch, mock_open
import os
from chakin import Chakin
from chakin.utils.csv_handler import CSVHandler

class TestChakin(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin()

    @patch('chakin.utils.csv_handler.pd.read_csv')
    def test_csv_handler_parse(self, mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({
            'Name': ['fastText(ar)'],
            'Dimension': [300],
            'Corpus': ['Wikipedia'],
            'VocabularySize': ['610K'],
            'Method': ['fastText'],
            'Language': ['Arabic'],
            'Paper': ['Enriching Word Vectors with Subword Information'],
            'Author': ['Facebook'],
            'URL': ['https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ar.300.vec.gz']
        })
        csv_handler = CSVHandler()
        datasets = csv_handler.parseCSV()
        self.assertEqual(len(datasets), 1)
        self.assertEqual(datasets[0].name, 'fastText(ar)')

    def test_search(self):
        results = self.chakin.search(lang='Arabic')
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0].language, 'Arabic')

    @patch('chakin.Chakin._download_file')
    def test_download(self, mock_download_file):
        mock_download_file.return_value = None
        self.chakin.download(number=0, save_dir='./')
        mock_download_file.assert_called_once()

    @patch('os.makedirs')
    @patch('os.path.exists')
    def test_download_directory_creation(self, mock_exists, mock_makedirs):
        mock_exists.return_value = False
        self.chakin.download(number=0, save_dir='./new_dir')
        mock_makedirs.assert_called_once_with('./new_dir')

if __name__ == '__main__':
    unittest.main()
