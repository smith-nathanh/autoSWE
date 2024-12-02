import argparse
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator

class CLI:
    def parse_arguments(self, args):
        parser = argparse.ArgumentParser(description='Convert CSV to JSON')
        parser.add_argument('--delimiters', nargs='*', default=[','], help='List of delimiters')
        parser.add_argument('--schema', type=str, help='JSON schema as a string')
        parser.add_argument('csv_filepath', type=str, help='Path to the input CSV file')
        parser.add_argument('json_filepath', type=str, help='Path to the output JSON file')
        return vars(parser.parse_args(args))

    def execute_conversion(self, args):
        csv_parser = CSVParser(args['csv_filepath'], args['delimiters'][0])
        csv_parser.read_csv()
        data = [csv_parser.extract_column_names()] + csv_parser.extract_data_rows()

        json_generator = JSONGenerator()
        schema = json.loads(args['schema']) if args['schema'] else None
        json_data = json_generator.convert_to_json(data, schema)

        json_generator.output_json(json_data, args['json_filepath'])
