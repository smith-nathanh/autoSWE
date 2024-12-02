
import unittest
import os
from chakin.chakin import Chakin

class TestChakinFeatures(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin(csv_path='chakin/datasets.csv')
        self.test_dir = 'test_downloads'
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

    def tearDown(self):
        # Clean up the test directory after tests
        for file in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        os.rmdir(self.test_dir)

    def test_search_by_language(self):
        # Test searching for Arabic word vectors
        results = self.chakin.search(lang='Arabic')
        self.assertIn('fastText(ar)', results)

        # Test searching for German word vectors
        results = self.chakin.search(lang='German')
        self.assertIn('fastText(de)', results)

    def test_download_vector(self):
        # Test downloading a word vector
        # This test assumes the network is available and the URL is correct
        # In a real-world scenario, you would mock the requests.get call
        self.chakin.download(number=0, save_dir=self.test_dir)
        downloaded_file = os.path.join(self.test_dir, 'cc.ar.300.vec.gz')
        self.assertTrue(os.path.exists(downloaded_file))

if __name__ == '__main__':
    unittest.main()
