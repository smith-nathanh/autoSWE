import unittest
import json
import os
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator
from hone.cli import CLI

class TestHoneFeatures(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()
        self.test_data_dir = 'HoneProject/data_file/'

    def test_csv_parsing(self):
        # Test CSV parsing with comma delimiter
        csv_parser = CSVParser(os.path.join(self.test_data_dir, 'comma_test/dataset.csv'))
        csv_parser.read_csv()
        self.assertEqual(csv_parser.extract_column_names(), ['"test","ing"', ' "beep"""'])
        self.assertEqual(csv_parser.extract_data_rows(), [['"1', '"2']])

    def test_json_generation_without_schema(self):
        # Test JSON generation without schema
        csv_parser = CSVParser(os.path.join(self.test_data_dir, 'quotes_test/dataset.csv'))
        csv_parser.read_csv()
        data = [csv_parser.extract_column_names()] + csv_parser.extract_data_rows()

        json_generator = JSONGenerator()
        json_data = json_generator.convert_to_json(data)

        expected_json = [
            {
                "some 'quoted"' field"": "no quotes",
                "adopted_since": "2012",
                "adopted": "TRUE",
                "birth": {
                    "year": "2011",
                    "month": "April",
                    "day": "11"
                },
                "weight (kg)": "3.6",
                "age (years)": "5",
                "name": "Tommy"
            }
        ]

        self.assertEqual(json_data, expected_json)

    def test_json_generation_with_schema(self):
        # Test JSON generation with schema
        csv_parser = CSVParser(os.path.join(self.test_data_dir, 'small_cats_dataset/dataset.csv'))
        csv_parser.read_csv()
        data = [csv_parser.extract_column_names()] + csv_parser.extract_data_rows()

        json_generator = JSONGenerator()
        with open(os.path.join(self.test_data_dir, 'small_cats_dataset/nested_schema.json')) as schema_file:
            schema = json.load(schema_file)

        json_data = json_generator.convert_to_json(data, schema)

        expected_json = [
            {
                "adopted": "TRUE",
                "adopted_since": "2012",
                "age (years)": "5",
                "birth": {
                    "day": "11",
                    "month": "April",
                    "year": "2011"
                },
                "name": "Tommy",
                "weight (kg)": "3.6"
            },
            {
                "adopted": "FALSE",
                "adopted_since": "N/A",
                "age (years)": "2",
                "birth": {
                    "day": "6",
                    "month": "May",
                    "year": "2015"
                },
                "name": "Clara",
                "weight (kg)": "8.2"
            }
        ]

        self.assertEqual(json_data, expected_json)

    def test_cli_execution(self):
        # Test CLI execution
        args = [
            '--delimiters', ',',
            '--schema', json.dumps({
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
            }),
            os.path.join(self.test_data_dir, 'small_cats_dataset/dataset.csv'),
            os.path.join(self.test_data_dir, 'small_cats_dataset/output.json')
        ]

        parsed_args = self.cli.parse_arguments(args)
        self.cli.execute_conversion(parsed_args)

        with open(os.path.join(self.test_data_dir, 'small_cats_dataset/output.json')) as output_file:
            json_data = json.load(output_file)

        expected_json = [
            {
                "adopted": "TRUE",
                "adopted_since": "2012",
                "age (years)": "5",
                "birth": {
                    "day": "11",
                    "month": "April",
                    "year": "2011"
                },
                "name": "Tommy",
                "weight (kg)": "3.6"
            },
            {
                "adopted": "FALSE",
                "adopted_since": "N/A",
                "age (years)": "2",
                "birth": {
                    "day": "6",
                    "month": "May",
                    "year": "2015"
                },
                "name": "Clara",
                "weight (kg)": "8.2"
            }
        ]

        self.assertEqual(json_data, expected_json)

if __name__ == '__main__':
    unittest.main()
