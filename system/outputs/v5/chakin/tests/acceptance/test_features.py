import unittest
import os
from chakin import Chakin

class TestChakinFeatures(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin(dataset_path='chakin/datasets.csv')

    def test_search_by_language(self):
        # Test searching for Arabic word vectors
        results = self.chakin.search(lang='Arabic')
        self.assertTrue(any('Arabic' in str(vector) for vector in results))

        # Test searching for German word vectors
        results = self.chakin.search(lang='German')
        self.assertTrue(any('German' in str(vector) for vector in results))

    def test_download_valid_vector(self):
        # Test downloading a valid vector
        try:
            self.chakin.download(number=0, save_dir='./')
            self.assertTrue(os.path.exists('./cc.ar.300.vec.gz'))
        finally:
            if os.path.exists('./cc.ar.300.vec.gz'):
                os.remove('./cc.ar.300.vec.gz')

    def test_download_invalid_number(self):
        # Test downloading with an invalid number
        with self.assertRaises(ValueError):
            self.chakin.download(number=10, save_dir='./')

    def test_progress_bar(self):
        # Test if progress bar messages are printed
        with self.assertLogs() as log:
            self.chakin._download_vector(url='https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ar.300.vec.gz', save_dir='./')
            self.assertIn('Download started...', log.output[0])
            self.assertIn('Download finished!', log.output[-1])

if __name__ == '__main__':
    unittest.main()
