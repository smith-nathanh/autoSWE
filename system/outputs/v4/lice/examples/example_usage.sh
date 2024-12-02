#!/bin/bash

# Generate a BSD3 license using default options
python src/core.py bsd3

# Generate an MIT license using default options
python src/core.py mit

# Generate a GPL3 license for the year 2021 and organization 'ExampleOrg'
python src/core.py gpl3 --year 2021 --org 'ExampleOrg'

# Generate an Apache license with a header formatted for a Python source file
python src/core.py apache --header --language py

# Generate a BSD2 license and save it to a file named 'LICENSE'
python src/core.py bsd2 --file LICENSE
