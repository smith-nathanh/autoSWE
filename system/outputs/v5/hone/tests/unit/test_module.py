
import unittest
import json
from unittest.mock import patch, mock_open
from src.csv_parser import CSVParser
from src.json_generator import JSONGenerator
from src.file_manager import FileManager
from src.cli import CLI
import argparse

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

    def test_empty_file(self):
        parser = CSVParser('data_file/comma_test/empty.csv')
        parser.read_csv()
        self.assertEqual(parser.extract_column_names(), [])
        self.assertEqual(parser.extract_data_rows(), [])

    def test_invalid_file_path(self):
        with self.assertRaises(FileNotFoundError):
            parser = CSVParser('invalid_path.csv')
            parser.read_csv()

class TestJSONGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = JSONGenerator()
        self.data = [['name', 'age'], ['Tommy', '5'], ['Clara', '2']]
        self.schema = {'name': 'name', 'age': 'age'}

    def test_convert_to_json_with_schema(self):
        expected = [
            {'name': 'Tommy', 'age': '5'},
            {'name': 'Clara', 'age': '2'}
        ]
        result = self.generator.convert_to_json(self.data, self.schema)
        self.assertEqual(result, expected)

    def test_convert_to_json_without_schema(self):
        expected = [
            {'name': 'Tommy', 'age': '5'},
            {'name': 'Clara', 'age': '2'}
        ]
        result = self.generator.convert_to_json(self.data)
        self.assertEqual(result, expected)

    def test_empty_data(self):
        result = self.generator.convert_to_json([])
        self.assertEqual(result, [])

    def test_invalid_schema(self):
        with self.assertRaises(KeyError):
            self.generator.convert_to_json(self.data, {'invalid': 'key'})

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager()

    def test_open_and_close_file(self):
        file = self.file_manager.open_file('data_file/comma_test/dataset.csv', 'r')
        self.assertFalse(file.closed)
        self.file_manager.close_file(file)
        self.assertTrue(file.closed)

    def test_open_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            self.file_manager.open_file('invalid_path.csv', 'r')

class TestCLI(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(csv_filepath='data_file/comma_test/dataset.csv',
                                           json_filepath='data_file/comma_test/output.json',
                                           delimiters=',',
                                           schema=None))
    def test_parse_arguments(self, mock_args):
        cli = CLI()
        args = cli.parse_arguments()
        self.assertEqual(args['csv_filepath'], 'data_file/comma_test/dataset.csv')
        self.assertEqual(args['json_filepath'], 'data_file/comma_test/output.json')
        self.assertEqual(args['delimiters'], ',')
        self.assertIsNone(args['schema'])

    @patch('builtins.open', new_callable=mock_open)
    @patch('src.csv_parser.CSVParser.read_csv')
    @patch('src.json_generator.JSONGenerator.output_json')
    def test_execute_conversion(self, mock_output_json, mock_read_csv, mock_file):
        cli = CLI()
        args = {
            'csv_filepath': 'data_file/comma_test/dataset.csv',
            'json_filepath': 'data_file/comma_test/output.json',
            'delimiters': ',',
            'schema': None
        }
        cli.execute_conversion(args)
        mock_read_csv.assert_called_once()
        mock_output_json.assert_called_once()

if __name__ == '__main__':
    unittest.main()
