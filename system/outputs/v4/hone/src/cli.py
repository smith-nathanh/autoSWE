import argparse
from .csv_parser import CSVParser
from .json_generator import JSONGenerator

class CLI:
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Convert CSV to JSON.')
        parser.add_argument('csv_filepath', type=str, help='Path to the input CSV file.')
        parser.add_argument('json_filepath', type=str, help='Path to the output JSON file.')
        parser.add_argument('--delimiters', type=str, default=',', help='Delimiter for the CSV file.')
        parser.add_argument('--schema', type=str, help='JSON schema as a string.')
        return vars(parser.parse_args())

    def execute_conversion(self, args):
        csv_parser = CSVParser(args['csv_filepath'], args['delimiters'])
        csv_parser.read_csv()
        data = csv_parser.extract_data_rows()
        column_names = csv_parser.extract_column_names()

        schema = json.loads(args['schema']) if args['schema'] else None

        json_generator = JSONGenerator()
        json_data = json_generator.convert_to_json([column_names] + data, schema)
        json_generator.output_json(json_data, args['json_filepath'])

if __name__ == '__main__':
    cli = CLI()
    args = cli.parse_arguments()
    cli.execute_conversion(args)
