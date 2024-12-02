
import unittest
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator
from hone.cli import CLI
import json

class TestCSVParser(unittest.TestCase):
    def setUp(self):
        self.parser = CSVParser()

    def test_read_csv(self):
        data = self.parser.read_csv('hone_project/data_file/comma_test/dataset.csv')
        expected = [
            {"test,ing": "1", " beep""": "2"}
        ]
        self.assertEqual(data, expected)

    def test_extract_column_names(self):
        data = self.parser.read_csv('hone_project/data_file/comma_test/dataset.csv')
        column_names = self.parser.extract_column_names(data)
        expected = ["test,ing", " beep"""]
        self.assertEqual(column_names, expected)

    def test_extract_data_rows(self):
        data = self.parser.read_csv('hone_project/data_file/comma_test/dataset.csv')
        data_rows = self.parser.extract_data_rows(data)
        expected = [
            {"test,ing": "1", " beep""": "2"}
        ]
        self.assertEqual(data_rows, expected)

class TestJSONGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = JSONGenerator()

    def test_convert_to_json(self):
        data = [
            {"test,ing": "1", " beep""": "2"}
        ]
        json_data = self.generator.convert_to_json(data)
        expected = json.dumps(data, indent=4, sort_keys=True)
        self.assertEqual(json_data, expected)

    def test_output_json(self):
        data = json.dumps([{"test,ing": "1", " beep""": "2"}], indent=4, sort_keys=True)
        self.generator.output_json(data, 'hone_project/data_file/comma_test/output.json')
        with open('hone_project/data_file/comma_test/output.json', 'r') as file:
            content = file.read()
        self.assertEqual(content, data)

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()

    def test_parse_arguments(self):
        args = ['hone_project/data_file/comma_test/dataset.csv', 'hone_project/data_file/comma_test/output.json']
        parsed_args = self.cli.parse_arguments(args)
        expected = {
            'csv_filepath': 'hone_project/data_file/comma_test/dataset.csv',
            'json_filepath': 'hone_project/data_file/comma_test/output.json',
            'delimiters': ',',
            'schema': None
        }
        self.assertEqual(parsed_args, expected)

    def test_execute_conversion(self):
        args = {
            'csv_filepath': 'hone_project/data_file/comma_test/dataset.csv',
            'json_filepath': 'hone_project/data_file/comma_test/output.json',
            'delimiters': ',',
            'schema': None
        }
        self.cli.execute_conversion(args)
        with open('hone_project/data_file/comma_test/output.json', 'r') as file:
            content = json.load(file)
        expected = [
            {"test,ing": "1", " beep""": "2"}
        ]
        self.assertEqual(content, expected)

if __name__ == '__main__':
    unittest.main()
