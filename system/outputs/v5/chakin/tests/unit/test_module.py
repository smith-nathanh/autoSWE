import unittest
from chakin import Chakin
import os

class TestChakin(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin(dataset_path='chakin/datasets.csv')

    def test_search_valid_language(self):
        results = self.chakin.search(lang='Arabic')
        self.assertTrue(any('Arabic' in str(vector) for vector in results))

    def test_search_invalid_language(self):
        results = self.chakin.search(lang='Klingon')
        self.assertEqual(len(results), 0)

    def test_download_valid_number(self):
        # Assuming the dataset has at least 1 entry
        try:
            self.chakin.download(number=0, save_dir='./')
            self.assertTrue(os.path.exists('./cc.ar.300.vec.gz'))
        finally:
            if os.path.exists('./cc.ar.300.vec.gz'):
                os.remove('./cc.ar.300.vec.gz')

    def test_download_invalid_number(self):
        with self.assertRaises(ValueError):
            self.chakin.download(number=10, save_dir='./')

    def test_download_negative_number(self):
        with self.assertRaises(ValueError):
            self.chakin.download(number=-1, save_dir='./')

if __name__ == '__main__':
    unittest.main()
