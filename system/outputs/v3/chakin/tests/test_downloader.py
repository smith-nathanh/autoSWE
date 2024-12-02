import unittest
from chakin import Chakin

class TestChakin(unittest.TestCase):
    def setUp(self):
        self.chakin = Chakin()

    def test_search(self):
        results = self.chakin.search(lang='Arabic')
        self.assertTrue(len(results) > 0)

    def test_download(self):
        # This is a placeholder test; actual download tests would require mocking network calls
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
