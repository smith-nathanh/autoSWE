import unittest
import json
import os
from src.csv_parser import CSVParser
from src.json_generator import JSONGenerator
from src.cli import CLI

class TestFeatures(unittest.TestCase):
    def setUp(self):
        # Setup paths for test files
        self.comma_test_csv = 'data_file/comma_test/dataset.csv'
        self.comma_test_json = 'data_file/comma_test/output.json'
        self.quotes_test_csv = 'data_file/quotes_test/dataset.csv'
        self.quotes_test_json = 'data_file/quotes_test/output.json'
        self.small_cats_csv = 'data_file/small_cats_dataset/dataset.csv'
        self.small_cats_json = 'data_file/small_cats_dataset/output.json'
        self.small_cats_schema = 'data_file/small_cats_dataset/nested_schema.json'

    def test_csv_to_json_conversion_with_schema(self):
        # Test conversion with schema
        with open(self.small_cats_schema, 'r') as schema_file:
            schema = json.load(schema_file)

        csv_parser = CSVParser(self.small_cats_csv)
        csv_parser.read_csv()
        data = csv_parser.extract_data_rows()

        json_generator = JSONGenerator()
        json_data = json_generator.convert_to_json(data, schema)

        with open(self.small_cats_json, 'w') as json_file:
            json_generator.output_json(json_data, json_file)

        with open(self.small_cats_json, 'r') as json_file:
            output_data = json.load(json_file)

        with open('data_file/small_cats_dataset/nested_dataset.json', 'r') as expected_file:
            expected_data = json.load(expected_file)

        self.assertEqual(output_data, expected_data)

    def test_csv_to_json_conversion_without_schema(self):
        # Test conversion without schema
        csv_parser = CSVParser(self.quotes_test_csv)
        csv_parser.read_csv()
        data = csv_parser.extract_data_rows()

        json_generator = JSONGenerator()
        json_data = json_generator.convert_to_json(data)

        with open(self.quotes_test_json, 'w') as json_file:
            json_generator.output_json(json_data, json_file)

        with open(self.quotes_test_json, 'r') as json_file:
            output_data = json.load(json_file)

        with open('data_file/quotes_test/nested_dataset.json', 'r') as expected_file:
            expected_data = json.load(expected_file)

        self.assertEqual(output_data, expected_data)

    def test_cli_execution(self):
        # Test CLI execution
        cli = CLI()
        args = {
            'csv_filepath': self.comma_test_csv,
            'json_filepath': self.comma_test_json,
            'delimiters': ',',
            'schema': None
        }
        cli.execute_conversion(args)

        with open(self.comma_test_json, 'r') as json_file:
            output_data = json.load(json_file)

        with open('data_file/comma_test/nested_dataset.json', 'r') as expected_file:
            expected_data = json.load(expected_file)

        self.assertEqual(output_data, expected_data)

if __name__ == '__main__':
    unittest.main()
