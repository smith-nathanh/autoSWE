#!/bin/bash

# Additional example usage of the lice tool

# List template variables for a GPL3 license
python ../lice/core.py list-vars gpl3

# Use a custom template to generate a license
python ../lice/core.py custom-template ../lice/templates/template-custom.txt --year 2022 --org 'CustomOrg'