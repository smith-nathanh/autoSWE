import argparse
from .csv_parser import CSVParser
from .json_generator import JSONGenerator
from .file_manager import FileManager

class CLI:
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Convert CSV to JSON')
        parser.add_argument('csv_filepath', type=str, help='Path to the input CSV file')
        parser.add_argument('json_filepath', type=str, help='Path to the output JSON file')
        parser.add_argument('--delimiters', type=str, default=',', help='Delimiter for the CSV file')
        parser.add_argument('--schema', type=str, help='JSON schema as a string')
        return vars(parser.parse_args())

    def execute_conversion(self, args):
        csv_parser = CSVParser(args['csv_filepath'], args['delimiters'])
        csv_parser.read_csv()
        data = csv_parser.extract_data_rows()

        schema = None
        if args['schema']:
            schema = json.loads(args['schema'])

        json_generator = JSONGenerator()
        json_data = json_generator.convert_to_json(data, schema)

        file_manager = FileManager()
        with file_manager.open_file(args['json_filepath'], 'w') as file:
            json_generator.output_json(json_data, file)
