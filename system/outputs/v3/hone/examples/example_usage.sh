#!/bin/bash

# Example usage of the Hone project

# Convert a CSV file to JSON using the demo script
python demo.py --csv_filepath ../data_file/comma_test/dataset.csv --json_filepath ../data_file/comma_test/output.json

# Convert a CSV file to JSON with a custom schema
python demo.py --csv_filepath ../data_file/small_cats_dataset/dataset.csv --json_filepath ../data_file/small_cats_dataset/output.json --schema '{"birth": {"year": "birth year", "month": "birth month", "day": "birth day"}, "name": "name", "age (years)": "age (years)", "weight (kg)": "weight (kg)", "adopted": "adopted", "adopted_since": "adopted_since"}'