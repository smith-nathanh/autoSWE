import unittest
from unittest.mock import patch, mock_open
from chakin.chakin import Chakin
from chakin.csv_handler import CSVHandler
import os

class TestChakin(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin(csv_path='chakin/datasets.csv')

    def test_search_valid_language(self):
        results = self.chakin.search(lang='Arabic')
        self.assertIn('fastText(ar)', results)

    def test_search_invalid_language(self):
        results = self.chakin.search(lang='NonExistentLanguage')
        self.assertEqual(results, [])

    @patch('chakin.chakin.requests.get')
    def test_download(self, mock_get):
        # Mock the response to simulate a file download
        mock_get.return_value.iter_content = lambda chunk_size: [b'data'] * 5
        mock_get.return_value.headers = {'content-length': '20'}

        with patch('builtins.open', mock_open()) as mocked_file:
            self.chakin.download(number=0, save_dir='./test_dir')
            mocked_file.assert_called_once_with('./test_dir/cc.ar.300.vec.gz', 'wb')

    def test_csv_loading(self):
        csv_handler = CSVHandler()
        datasets = csv_handler.load_csv('chakin/datasets.csv')
        self.assertGreater(len(datasets), 0)
        self.assertEqual(datasets[0].Name, 'fastText(ar)')

    def test_progress_bar(self):
        from chakin.progress_bar import ProgressBar
        progress_bar = ProgressBar(total=100)
        progress_bar.update(50)
        self.assertEqual(progress_bar.current, 50)

if __name__ == '__main__':
    unittest.main()
