import unittest
import os
from chakin import Chakin

class TestChakinFeatures(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin()

    def test_search_by_language(self):
        # Test searching for Arabic word vectors
        results = self.chakin.search(lang='Arabic')
        self.assertTrue(len(results) > 0)
        self.assertTrue(any('Arabic' in result.language for result in results))

        # Test searching for English word vectors
        results = self.chakin.search(lang='English')
        self.assertTrue(len(results) > 0)
        self.assertTrue(any('English' in result.language for result in results))

    def test_download_vectors(self):
        # Test downloading a word vector
        save_dir = './test_vectors'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        try:
            self.chakin.download(number=0, save_dir=save_dir)
            file_path = os.path.join(save_dir, 'fastText(ar).vec.gz')
            self.assertTrue(os.path.exists(file_path))
        finally:
            # Clean up downloaded file
            if os.path.exists(file_path):
                os.remove(file_path)
            if os.path.exists(save_dir):
                os.rmdir(save_dir)

if __name__ == '__main__':
    unittest.main()
