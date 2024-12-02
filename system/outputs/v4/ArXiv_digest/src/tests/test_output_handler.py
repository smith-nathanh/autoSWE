import unittest
import os
import csv
from src.utils.output_handler import OutputHandler

class TestOutputHandler(unittest.TestCase):
    def setUp(self):
        self.data = [
            {
                'category': 'cs.CL',
                'title': 'Sample Title',
                'author': 'Author Name',
                'abstract': 'Sample abstract.',
                'published': '2023-10-01T00:00:00Z',
                'link': 'http://arxiv.org/abs/1234.5678v1'
            }
        ]
        self.file_path = 'test_output.csv'

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_print_to_console(self):
        output_handler = OutputHandler()
        output_handler.printToConsole(self.data)
        # This test is visual, ensure it prints correctly to console

    def test_save_to_csv(self):
        output_handler = OutputHandler()
        output_handler.saveToCSV(self.data, self.file_path)
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]['category'], 'cs.CL')

if __name__ == '__main__':
    unittest.main()
