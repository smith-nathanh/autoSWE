import unittest
import os
from chakin.chakin import Chakin

class TestChakinFeatures(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin()

    def test_search_by_language(self):
        # Test searching for Arabic word vectors
        results = self.chakin.search('Arabic')
        self.assertTrue(len(results) > 0)
        self.assertTrue(any('Arabic' in dataset.language for dataset in results))

        # Test searching for English word vectors
        results = self.chakin.search('English')
        self.assertTrue(len(results) > 0)
        self.assertTrue(any('English' in dataset.language for dataset in results))

    def test_download_vectors(self):
        # Test downloading a specific word vector
        try:
            self.chakin.download(0, './')
            # Check if the file is downloaded (this is a placeholder check)
            # In a real scenario, you would check the actual file existence and integrity
            self.assertTrue(os.path.exists('./cc.ar.300.vec.gz'))
        except Exception as e:
            self.fail(f"Download failed with exception {e}")

    def tearDown(self):
        # Clean up downloaded files after tests
        try:
            os.remove('./cc.ar.300.vec.gz')
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()
