import argparse
import json
from hone.csv_parser import CSVParser
from hone.json_generator import JSONGenerator
from hone.utilities import Utilities


def main():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('--csv_filepath', type=str, required=True, help='Path to the input CSV file')
    parser.add_argument('--json_filepath', type=str, required=True, help='Path to the output JSON file')
    parser.add_argument('--delimiters', type=str, nargs='*', default=[','], help='List of delimiters for parsing CSV files')
    parser.add_argument('--schema', type=str, help='JSON schema structure for the output JSON')

    args = parser.parse_args()

    csv_parser = CSVParser()
    json_generator = JSONGenerator()
    utilities = Utilities()

    with utilities.open_file(args.csv_filepath, 'r') as csv_file:
        csv_parser.read_csv(csv_file, args.delimiters[0])
        data = csv_parser.extract_data_rows()

    schema = json.loads(args.schema) if args.schema else None
    json_data = json_generator.convert_to_json(data, schema)

    with utilities.open_file(args.json_filepath, 'w') as json_file:
        json_generator.output_json(json_data, json_file)


if __name__ == '__main__':
    main()