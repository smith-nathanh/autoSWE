import unittest
from chakin import Chakin

class TestChakin(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin(dataset_path='chakin/datasets.csv')

    def test_search(self):
        results = self.chakin.search(lang='Arabic')
        self.assertTrue(any('Arabic' in str(vector) for vector in results))

    def test_download_invalid_number(self):
        with self.assertRaises(ValueError):
            self.chakin.download(number=10, save_dir='./')

if __name__ == '__main__':
    unittest.main()
