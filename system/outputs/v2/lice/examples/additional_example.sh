#!/bin/bash

# List all template variables for the MIT license
python lice/core.py mit --vars

# Generate a custom license using a specified template
python lice/core.py custom --template ./templates/custom-template.txt