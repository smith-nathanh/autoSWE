import unittest
import os
import json
import subprocess
from src.csv_parser import CSVParser
from src.json_generator import JSONGenerator
from src.cli import CLI

class TestFeatures(unittest.TestCase):
    def setUp(self):
        # Define paths for test files
        self.csv_path = 'data_file/small_cats_dataset/dataset.csv'
        self.json_path = 'data_file/small_cats_dataset/output.json'
        self.schema = '{"adopted_since": "adopted_since", "adopted": "adopted", "birth": {"year": "birth year", "month": "birth month", "day": "birth day"}, "weight (kg)": "weight (kg)", "age (years)": "age (years)", "name": "name"}'

    def test_csv_to_json_conversion_with_schema(self):
        # Run the CLI command to convert CSV to JSON
        subprocess.run(['python', 'src/cli.py', self.csv_path, self.json_path, '--schema', self.schema])

        # Load the generated JSON file
        with open(self.json_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        # Load the expected JSON file
        with open('data_file/small_cats_dataset/nested_dataset.json', 'r', encoding='utf-8') as expected_file:
            expected_data = json.load(expected_file)

        # Assert that the generated JSON matches the expected JSON
        self.assertEqual(json_data, expected_data)

    def test_csv_to_json_conversion_without_schema(self):
        # Run the CLI command to convert CSV to JSON without schema
        subprocess.run(['python', 'src/cli.py', self.csv_path, self.json_path])

        # Load the generated JSON file
        with open(self.json_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        # Expected data without schema
        expected_data = [
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

        # Assert that the generated JSON matches the expected JSON
        self.assertEqual(json_data, expected_data)

if __name__ == '__main__':
    unittest.main()
