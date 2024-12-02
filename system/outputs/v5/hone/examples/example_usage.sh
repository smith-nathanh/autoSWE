#!/bin/bash

# Example usage of the CSV to JSON conversion
python ../src/cli.py ../data_file/small_cats_dataset/dataset.csv ../data_file/small_cats_dataset/output.json --schema '{"adopted_since": "adopted_since", "adopted": "adopted", "birth": {"year": "birth year", "month": "birth month", "day": "birth day"}, "weight (kg)": "weight (kg)", "age (years)": "age (years)", "name": "name"}'