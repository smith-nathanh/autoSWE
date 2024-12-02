import unittest
from src.csv_parser import CSVParser

class TestCSVParser(unittest.TestCase):
    def setUp(self):
        self.parser = CSVParser('data_file/comma_test/dataset.csv')
        self.parser.read_csv()

    def test_extract_column_names(self):
        expected = ['"test","ing"', ' "beep"""']
        self.assertEqual(self.parser.extract_column_names(), expected)

    def test_extract_data_rows(self):
        expected = [['"1', '"2']]
        self.assertEqual(self.parser.extract_data_rows(), expected)

if __name__ == '__main__':
    unittest.main()
