import unittest
import os
from chakin.chakin import Chakin

class TestChakin(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin()

    def test_search_valid_language(self):
        # Test searching for a valid language
        results = self.chakin.search('Arabic')
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0].language, 'Arabic')

    def test_search_invalid_language(self):
        # Test searching for an invalid language
        results = self.chakin.search('Klingon')
        self.assertEqual(len(results), 0)

    def test_download_valid_index(self):
        # Test downloading with a valid index
        try:
            self.chakin.download(0, './')
        except Exception as e:
            self.fail(f"Download failed with exception {e}")

    def test_download_invalid_index(self):
        # Test downloading with an invalid index
        with self.assertRaises(ValueError):
            self.chakin.download(10, './')

    def test_download_invalid_directory(self):
        # Test downloading to an invalid directory
        with self.assertRaises(OSError):
            self.chakin.download(0, '/invalid/directory')

if __name__ == '__main__':
    unittest.main()
