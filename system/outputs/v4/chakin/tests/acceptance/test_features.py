import unittest
import os
from chakin import Chakin

class TestChakinFeatures(unittest.TestCase):

    def setUp(self):
        self.chakin = Chakin()

    def test_search_by_language(self):
        # Test searching for English word vectors
        results = self.chakin.search('English')
        self.assertTrue(any('English' in result['Language'] for result in results))

        # Test searching for Arabic word vectors
        results = self.chakin.search('Arabic')
        self.assertTrue(any('Arabic' in result['Language'] for result in results))

    def test_download_vectors(self):
        # Test downloading a word vector
        save_dir = './test_downloads'
        os.makedirs(save_dir, exist_ok=True)
        self.chakin.download(0, save_dir)
        file_name = os.path.join(save_dir, 'cc.ar.300.vec.gz')
        self.assertTrue(os.path.exists(file_name))
        os.remove(file_name)
        os.rmdir(save_dir)

    def test_progress_tracking(self):
        # Test if progress bar is displayed during download
        # This is a bit tricky to test in a unit test, but we can ensure no exceptions are raised
        save_dir = './test_downloads'
        os.makedirs(save_dir, exist_ok=True)
        try:
            self.chakin.download(0, save_dir)
        except Exception as e:
            self.fail(f"Download raised an exception: {e}")
        finally:
            file_name = os.path.join(save_dir, 'cc.ar.300.vec.gz')
            if os.path.exists(file_name):
                os.remove(file_name)
            os.rmdir(save_dir)

if __name__ == '__main__':
    unittest.main()
