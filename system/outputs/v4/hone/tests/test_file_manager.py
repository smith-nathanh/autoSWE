import unittest
from src.file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.manager = FileManager()

    def test_open_and_close_file(self):
        file = self.manager.open_file('data_file/comma_test/dataset.csv', 'r')
        self.assertFalse(file.closed)
        self.manager.close_file(file)
        self.assertTrue(file.closed)

if __name__ == '__main__':
    unittest.main()