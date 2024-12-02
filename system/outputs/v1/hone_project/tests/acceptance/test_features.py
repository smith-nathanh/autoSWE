import unittest
import json
import os
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator
from hone.cli import CLI

class TestCSVToJSONConversion(unittest.TestCase):
    def setUp(self):
        self.csv_parser = CSVParser()
        self.json_generator = JSONGenerator()
        self.cli = CLI()

    def test_csv_parsing_with_comma_test(self):
        # Test CSV parsing for comma_test dataset
        data = self.csv_parser.read_csv('hone_project/data_file/comma_test/dataset.csv')
        expected_column_names = ['"test","ing"', ' "beep"""']
        expected_data_rows = [{'"test","ing"': '"1', ' "beep"""': '"2'}]

        self.assertEqual(self.csv_parser.extract_column_names(data), expected_column_names)
        self.assertEqual(self.csv_parser.extract_data_rows(data), expected_data_rows)

    def test_json_generation_with_comma_test(self):
        # Test JSON generation for comma_test dataset
        data = self.csv_parser.read_csv('hone_project/data_file/comma_test/dataset.csv')
        json_output = self.json_generator.convert_to_json(data)
        expected_json_output = json.dumps([
            {
                ' "beep"""': '"2',
                '"test","ing"': '"1'
            }
        ], indent=4, sort_keys=True)

        self.assertEqual(json_output, expected_json_output)

    def test_csv_parsing_with_quotes_test(self):
        # Test CSV parsing for quotes_test dataset
        data = self.csv_parser.read_csv('hone_project/data_file/quotes_test/dataset.csv')
        expected_column_names = [
            'name', 'age (years)', 'weight (kg)', 'birth day', 'birth month',
            'birth year', 'adopted', 'adopted_since', "some 'quoted' field"
        ]
        expected_data_rows = [
            {
                'name': 'Tommy', 'age (years)': '5', 'weight (kg)': '3.6',
                'birth day': '11', 'birth month': 'April', 'birth year': '2011',
                'adopted': 'TRUE', 'adopted_since': '2012', "some 'quoted' field": 'no quotes'
            }
        ]

        self.assertEqual(self.csv_parser.extract_column_names(data), expected_column_names)
        self.assertEqual(self.csv_parser.extract_data_rows(data), expected_data_rows)

    def test_json_generation_with_quotes_test(self):
        # Test JSON generation for quotes_test dataset
        data = self.csv_parser.read_csv('hone_project/data_file/quotes_test/dataset.csv')
        json_output = self.json_generator.convert_to_json(data)
        expected_json_output = json.dumps([
            {
                "some 'quoted\"' field\"": 'no quotes',
                'adopted_since': '2012',
                'adopted': 'TRUE',
                'birth': {
                    'year': '2011',
                    'month': 'April',
                    'day': '11'
                },
                'weight (kg)': '3.6',
                'age (years)': '5',
                'name': 'Tommy'
            }
        ], indent=4, sort_keys=True)

        self.assertEqual(json_output, expected_json_output)

    def test_csv_parsing_with_small_cats_dataset(self):
        # Test CSV parsing for small_cats_dataset
        data = self.csv_parser.read_csv('hone_project/data_file/small_cats_dataset/dataset.csv')
        expected_column_names = [
            'name', 'age (years)', 'weight (kg)', 'birth day', 'birth month',
            'birth year', 'adopted', 'adopted_since'
        ]
        expected_data_rows = [
            {
                'name': 'Tommy', 'age (years)': '5', 'weight (kg)': '3.6',
                'birth day': '11', 'birth month': 'April', 'birth year': '2011',
                'adopted': 'TRUE', 'adopted_since': '2012'
            },
            {
                'name': 'Clara', 'age (years)': '2', 'weight (kg)': '8.2',
                'birth day': '6', 'birth month': 'May', 'birth year': '2015',
                'adopted': 'FALSE', 'adopted_since': 'N/A'
            }
        ]

        self.assertEqual(self.csv_parser.extract_column_names(data), expected_column_names)
        self.assertEqual(self.csv_parser.extract_data_rows(data), expected_data_rows)

    def test_json_generation_with_small_cats_dataset(self):
        # Test JSON generation for small_cats_dataset
        data = self.csv_parser.read_csv('hone_project/data_file/small_cats_dataset/dataset.csv')
        schema = json.loads(open('hone_project/data_file/small_cats_dataset/nested_schema.json').read())
        json_output = self.json_generator.convert_to_json(data, schema)
        expected_json_output = json.dumps([
            {
                'adopted': 'TRUE',
                'adopted_since': '2012',
                'age (years)': '5',
                'birth': {
                    'day': '11',
                    'month': 'April',
                    'year': '2011'
                },
                'name': 'Tommy',
                'weight (kg)': '3.6'
            },
            {
                'adopted': 'FALSE',
                'adopted_since': 'N/A',
                'age (years)': '2',
                'birth': {
                    'day': '6',
                    'month': 'May',
                    'year': '2015'
                },
                'name': 'Clara',
                'weight (kg)': '8.2'
            }
        ], indent=4, sort_keys=True)

        self.assertEqual(json_output, expected_json_output)

if __name__ == '__main__':
    unittest.main()
