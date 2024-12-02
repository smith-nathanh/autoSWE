# Hone Project

## System Overview

The Hone project is designed to facilitate the conversion of CSV files into nested JSON formats. It aims to provide a robust and flexible solution for transforming flat CSV data structures into hierarchical JSON objects that are more suitable for various applications and data needs.

## Usage Instructions

To convert a CSV file to JSON with the command-line interface, use the following command:

```bash
python examples/demo.py --csv_filepath <path_to_csv> --json_filepath <path_to_json> [--delimiters <delimiters>] [--schema <schema>]
```

### Command Line Configuration Arguments

- `--delimiters` (list, optional) - List of string delimiters for parsing CSV files.
- `--schema` (JSON object as string, optional) - JSON schema structure for the output JSON.
- `csv_filepath` (string, required) - Path to the input CSV file.
- `json_filepath` (string, required) - Path to the output JSON file.

## Project Structure

- `hone/`: Contains the core modules for CSV parsing, JSON generation, utilities, and CLI.
- `examples/`: Contains example scripts and usage demonstrations.
- `data_file/`: Contains test datasets for validating the conversion process.

## Acceptance Criteria

The package should be capable of converting any valid CSV file to a structured JSON format. The output JSON should accurately reflect the structure defined by the schema or the inferred structure based on the CSV's column names.