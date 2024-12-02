# Hone Project

The Hone project is designed to facilitate the conversion of CSV files into nested JSON formats. It aims to provide a robust and flexible solution for transforming flat CSV data structures into hierarchical JSON objects that are more suitable for various applications and data needs.

## Features
- CSV Parsing with support for custom delimiters.
- JSON Generation with custom or automatically generated schema.
- Command-Line Interface for easy execution.

## Installation

To install the Hone package, clone the repository and navigate to the project directory:

```bash
$ git clone <repository-url>
$ cd HoneProject
```

## Usage

To convert a CSV file to JSON using the command-line interface, use the following command:

```bash
$ python examples/demo.py --csv_filepath <path_to_csv> --json_filepath <path_to_json>
```

## Command Line Arguments
- `--delimiters` (list, optional): List of string delimiters for parsing CSV files.
- `--schema` (JSON object as string, optional): JSON schema structure for the output JSON.
- `csv_filepath` (string, required): Path to the input CSV file.
- `json_filepath` (string, required): Path to the output JSON file.

## Project Structure

- `hone/`: Contains the core modules for CSV parsing, JSON generation, utilities, and CLI.
- `examples/`: Contains example scripts and usage demonstrations.
- `data_file/`: Contains test datasets for validation.

## Testing

To test the functionality, use the datasets provided in the `data_file/` directory. Run the demo script to see the conversion in action.

## License

This project is licensed under the MIT License.
