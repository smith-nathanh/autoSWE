import unittest
from chakin import Chakin
import os

class TestChakin(unittest.TestCase):

    def setUp(self):
        self.chakin = Chakin()

    def test_search(self):
        results = self.chakin.search('Arabic')
        self.assertTrue(any('Arabic' in result['Language'] for result in results))

    def test_download(self):
        save_dir = './test_downloads'
        os.makedirs(save_dir, exist_ok=True)
        self.chakin.download(0, save_dir)
        file_name = os.path.join(save_dir, 'cc.ar.300.vec.gz')
        self.assertTrue(os.path.exists(file_name))
        os.remove(file_name)
        os.rmdir(save_dir)

if __name__ == '__main__':
    unittest.main()
