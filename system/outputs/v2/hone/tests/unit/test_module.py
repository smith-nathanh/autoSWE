
import unittest
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator
import json
import os

class TestCSVParser(unittest.TestCase):
    def setUp(self):
        self.comma_test_csv = 'HoneProject/data_file/comma_test/dataset.csv'
        self.quotes_test_csv = 'HoneProject/data_file/quotes_test/dataset.csv'
        self.small_cats_csv = 'HoneProject/data_file/small_cats_dataset/dataset.csv'

    def test_read_csv_comma_test(self):
        parser = CSVParser(self.comma_test_csv)
        parser.read_csv()
        self.assertEqual(parser.extract_column_names(), ['"test","ing"', ' "beep"""'])
        self.assertEqual(parser.extract_data_rows(), [['"1', '"2']])

    def test_read_csv_quotes_test(self):
        parser = CSVParser(self.quotes_test_csv)
        parser.read_csv()
        self.assertEqual(parser.extract_column_names(), ['name', 'age (years)', 'weight (kg)', 'birth day', 'birth month', 'birth year', 'adopted', 'adopted_since', "some 'quoted' field"])
        self.assertEqual(parser.extract_data_rows(), [['Tommy', '5', '3.6', '11', 'April', '2011', 'TRUE', '2012', 'no quotes']])

    def test_read_csv_small_cats(self):
        parser = CSVParser(self.small_cats_csv)
        parser.read_csv()
        self.assertEqual(parser.extract_column_names(), ['name', 'age (years)', 'weight (kg)', 'birth day', 'birth month', 'birth year', 'adopted', 'adopted_since'])
        self.assertEqual(parser.extract_data_rows(), [['Tommy', '5', '3.6', '11', 'April', '2011', 'TRUE', '2012'], ['Clara', '2', '8.2', '6', 'May', '2015', 'FALSE', 'N/A']])

class TestJSONGenerator(unittest.TestCase):
    def setUp(self):
        self.json_generator = JSONGenerator()
        self.small_cats_data = [
            ['name', 'age (years)', 'weight (kg)', 'birth day', 'birth month', 'birth year', 'adopted', 'adopted_since'],
            ['Tommy', '5', '3.6', '11', 'April', '2011', 'TRUE', '2012'],
            ['Clara', '2', '8.2', '6', 'May', '2015', 'FALSE', 'N/A']
        ]
        self.small_cats_schema = {
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

    def test_convert_to_json_without_schema(self):
        expected_output = [
            {
                'name': 'Tommy',
                'age (years)': '5',
                'weight (kg)': '3.6',
                'birth day': '11',
                'birth month': 'April',
                'birth year': '2011',
                'adopted': 'TRUE',
                'adopted_since': '2012'
            },
            {
                'name': 'Clara',
                'age (years)': '2',
                'weight (kg)': '8.2',
                'birth day': '6',
                'birth month': 'May',
                'birth year': '2015',
                'adopted': 'FALSE',
                'adopted_since': 'N/A'
            }
        ]
        result = self.json_generator.convert_to_json(self.small_cats_data)
        self.assertEqual(result, expected_output)

    def test_convert_to_json_with_schema(self):
        expected_output = [
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
        result = self.json_generator.convert_to_json(self.small_cats_data, self.small_cats_schema)
        self.assertEqual(result, expected_output)

    def test_output_json(self):
        data = [{"name": "Tommy", "age": "5"}]
        filepath = 'test_output.json'
        self.json_generator.output_json(data, filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = json.load(f)
        self.assertEqual(content, data)
        os.remove(filepath)

if __name__ == '__main__':
    unittest.main()
