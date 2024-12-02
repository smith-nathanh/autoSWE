project-root/
│   README.md
│
├── lice/
│   ├── __init__.py
│   ├── core.py
│   ├── license_generator.py
│   ├── template_manager.py
│   ├── file_manager.py
│   └── config_manager.py
│
├── templates/
│   ├── template-afl3.txt
│   ├── template-agpl3.txt
│   ├── template-apache.txt
│   ├── template-bsd2.txt
│   ├── template-cc_by.txt
│   ├── ... (other license templates)
│   ├── template-agpl3-header.txt
│   ├── template-apache-header.txt
│   ├── template-cc_by-header.txt
│   └── ... (other header templates)
│
└── examples/
    ├── example_usage.sh
    └── additional_example.sh

README.md content:
# Lice Project

The `lice` project is a tool designed to streamline the creation of license files for software projects. It automates the retrieval and formatting of various open-source licenses, making it easier for developers to comply with legal requirements and share their code openly.

## Features
- Generate various licenses with simple commands.
- Customize the year and organization in the license.
- Integrate with `git config` or use `$USER` for default organization.
- Create license headers for different programming languages.
- Generate new source files with license headers.
- Detect programming language from file extension.
- Extendable to support additional licenses and languages.

## Usage
Refer to the `examples/example_usage.sh` for core functionality demonstration.

examples/example_usage.sh content:
```bash
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
```

additional_example.sh content:
```bash
#!/bin/bash

# List all template variables for the MIT license
python lice/core.py mit --vars

# Generate a custom license using a specified template
python lice/core.py custom --template ./templates/custom-template.txt
```