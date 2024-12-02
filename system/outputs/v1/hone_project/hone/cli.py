# cli.py

import argparse
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator

class CLI:
    def parse_arguments(self) -> Dict[str, Any]:
        parser = argparse.ArgumentParser(description='Convert CSV to JSON')
        parser.add_argument('csv_filepath', type=str, help='Path to the input CSV file')
        parser.add_argument('json_filepath', type=str, help='Path to the output JSON file')
        parser.add_argument('--delimiters', type=str, default=',', help='Delimiter for the CSV file')
        parser.add_argument('--schema', type=str, help='JSON schema structure for the output JSON')
        return vars(parser.parse_args())

    def execute_conversion(self, args: Dict[str, Any]):
        csv_parser = CSVParser()
        json_generator = JSONGenerator()

        data = csv_parser.read_csv(args['csv_filepath'], args['delimiters'])
        json_data = json_generator.convert_to_json(data, args.get('schema'))
        json_generator.output_json(json_data, args['json_filepath'])