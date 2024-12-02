import unittest
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator
from hone.utilities import Utilities
import json
import os

class TestCSVParser(unittest.TestCase):
    def setUp(self):
        self.csv_parser = CSVParser()
        self.test_csv_path = 'data_file/comma_test/dataset.csv'

    def test_read_csv(self):
        self.csv_parser.read_csv(self.test_csv_path)
        expected_columns = ['"test","ing"', ' "beep"""']
        expected_data = [['"1', '"2']]
        self.assertEqual(self.csv_parser.extract_column_names(), expected_columns)
        self.assertEqual(self.csv_parser.extract_data_rows(), expected_data)

class TestJSONGenerator(unittest.TestCase):
    def setUp(self):
        self.json_generator = JSONGenerator()
        self.csv_parser = CSVParser()
        self.csv_parser.read_csv('data_file/small_cats_dataset/dataset.csv')
        self.data = self.csv_parser.extract_data_rows()
        self.schema = {
            "adopted_since": "adopted_since",
            "adopted": "adopted",
            "birth": {
                "year": "birth year",
                "month": "birth month",
                "day": "birth day"
            },
            "weight (kg)": "weight (kg)",
            "age (years)": "age (years)",
            "name": "name"
        }

    def test_convert_to_json_with_schema(self):
        json_data = self.json_generator.convert_to_json(self.data, self.schema)
        expected_json_path = 'data_file/small_cats_dataset/nested_dataset.json'
        with open(expected_json_path, 'r') as file:
            expected_json_data = json.load(file)
        self.assertEqual(json_data, expected_json_data)

    def test_convert_to_json_without_schema(self):
        json_data = self.json_generator.convert_to_json(self.data)
        expected_json = [
            {
                "name": "Tommy",
                "age (years)": "5",
                "weight (kg)": "3.6",
                "birth day": "11",
                "birth month": "April",
                "birth year": "2011",
                "adopted": "TRUE",
                "adopted_since": "2012"
            },
            {
                "name": "Clara",
                "age (years)": "2",
                "weight (kg)": "8.2",
                "birth day": "6",
                "birth month": "May",
                "birth year": "2015",
                "adopted": "FALSE",
                "adopted_since": "N/A"
            }
        ]
        self.assertEqual(json_data, expected_json)

class TestUtilities(unittest.TestCase):
    def setUp(self):
        self.utilities = Utilities()

    def test_open_file(self):
        test_file_path = 'data_file/comma_test/column_names.csv'
        with self.utilities.open_file(test_file_path, 'r') as file:
            content = file.read()
        self.assertTrue(content.startswith('"""test"",""ing""," "beep"""""'))

if __name__ == '__main__':
    unittest.main()
