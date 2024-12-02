import unittest
from chakin.chakin import Chakin

class TestChakin(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin()

    def test_search(self):
        results = self.chakin.search('Arabic')
        self.assertTrue(len(results) > 0)

    def test_download(self):
        # This is a placeholder test; actual download logic would be needed
        try:
            self.chakin.download(0, './')
        except Exception as e:
            self.fail(f"Download failed with exception {e}")

if __name__ == '__main__':
    unittest.main()