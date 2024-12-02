import os
import subprocess

# Define the paths
csv_path = os.path.join('..', 'data_file', 'small_cats_dataset', 'dataset.csv')
json_path = os.path.join('..', 'data_file', 'small_cats_dataset', 'output.json')
schema = '{"adopted_since": "adopted_since", "adopted": "adopted", "birth": {"year": "birth year", "month": "birth month", "day": "birth day"}, "weight (kg)": "weight (kg)", "age (years)": "age (years)", "name": "name"}'

# Run the CLI command
subprocess.run(['python', '../src/cli.py', csv_path, json_path, '--schema', schema])