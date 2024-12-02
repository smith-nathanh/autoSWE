#!/bin/bash

# Generate a BSD3 license using default options
python lice/core.py bsd3

# Generate an MIT license using default options
python lice/core.py mit

# Generate a GPL3 license for the year 2021 and organization 'ExampleOrg'
python lice/core.py gpl3 --year 2021 --org 'ExampleOrg'

# Generate an Apache license with a header formatted for a Python source file
python lice/core.py apache --header --language py

# Generate a BSD2 license and save it to a file named 'LICENSE'
python lice/core.py bsd2 --file LICENSE