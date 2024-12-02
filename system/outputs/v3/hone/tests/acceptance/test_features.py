import unittest
import json
import os
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator
from hone.utilities import Utilities

class TestCSVToJSONConversion(unittest.TestCase):
    def setUp(self):
        self.csv_parser = CSVParser()
        self.json_generator = JSONGenerator()
        self.utilities = Utilities()

    def test_comma_test_conversion(self):
        # Test conversion for comma_test dataset
        csv_filepath = 'data_file/comma_test/dataset.csv'
        json_filepath = 'data_file/comma_test/output.json'
        expected_json_filepath = 'data_file/comma_test/nested_dataset.json'

        with self.utilities.open_file(csv_filepath, 'r') as csv_file:
            self.csv_parser.read_csv(csv_file, ',')
            data = self.csv_parser.extract_data_rows()

        json_data = self.json_generator.convert_to_json(data)

        with self.utilities.open_file(json_filepath, 'w') as json_file:
            self.json_generator.output_json(json_data, json_file)

        with open(expected_json_filepath, 'r') as expected_file:
            expected_json = json.load(expected_file)

        with open(json_filepath, 'r') as output_file:
            output_json = json.load(output_file)

        self.assertEqual(output_json, expected_json)

    def test_quotes_test_conversion(self):
        # Test conversion for quotes_test dataset
        csv_filepath = 'data_file/quotes_test/dataset.csv'
        json_filepath = 'data_file/quotes_test/output.json'
        expected_json_filepath = 'data_file/quotes_test/nested_dataset.json'

        with self.utilities.open_file(csv_filepath, 'r') as csv_file:
            self.csv_parser.read_csv(csv_file, ',')
            data = self.csv_parser.extract_data_rows()

        json_data = self.json_generator.convert_to_json(data)

        with self.utilities.open_file(json_filepath, 'w') as json_file:
            self.json_generator.output_json(json_data, json_file)

        with open(expected_json_filepath, 'r') as expected_file:
            expected_json = json.load(expected_file)

        with open(json_filepath, 'r') as output_file:
            output_json = json.load(output_file)

        self.assertEqual(output_json, expected_json)

    def test_small_cats_dataset_conversion_with_schema(self):
        # Test conversion for small_cats_dataset with schema
        csv_filepath = 'data_file/small_cats_dataset/dataset.csv'
        json_filepath = 'data_file/small_cats_dataset/output.json'
        expected_json_filepath = 'data_file/small_cats_dataset/nested_dataset.json'
        schema_filepath = 'data_file/small_cats_dataset/nested_schema.json'

        with open(schema_filepath, 'r') as schema_file:
            schema = json.load(schema_file)

        with self.utilities.open_file(csv_filepath, 'r') as csv_file:
            self.csv_parser.read_csv(csv_file, ',')
            data = self.csv_parser.extract_data_rows()

        json_data = self.json_generator.convert_to_json(data, schema)

        with self.utilities.open_file(json_filepath, 'w') as json_file:
            self.json_generator.output_json(json_data, json_file)

        with open(expected_json_filepath, 'r') as expected_file:
            expected_json = json.load(expected_file)

        with open(json_filepath, 'r') as output_file:
            output_json = json.load(output_file)

        self.assertEqual(output_json, expected_json)

if __name__ == '__main__':
    unittest.main()
