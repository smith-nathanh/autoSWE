project-root/
│   README.md
│   query_arxiv.py
│
├───examples/
│       example_usage.sh
│       example_query_1.txt
│       example_query_2.txt
│
└───src/
    │   __init__.py
    │   query_arxiv.py
    │
    ├───utils/
    │       __init__.py
    │       api_interaction.py
    │       xml_parser.py
    │       output_handler.py
    │       command_line_interface.py
    │
    └───tests/
            test_query_arxiv.py
            test_api_interaction.py
            test_xml_parser.py
            test_output_handler.py
            test_command_line_interface.py

README.md content:
# Query ArXiv

Query ArXiv is a Python-based tool designed to streamline the process of fetching research papers from the ArXiv database. It allows users to perform advanced searches based on parameters like category, author, title, and abstract, with an added feature to filter results based on recent publication dates.

## Features
- Advanced query options with flexible parameters.
- Time-based filtering to fetch recent papers.
- Output options for console display and CSV export.

## Usage
To execute a query, run the following script:

```bash
python query_arxiv.py \
--category [category] \
--title [title] \
--author [author] \
--abstract [abstract] \
--recent_days [number_of_days] \
[--to_file path_to_csv_file] \
[--verbose]
```

## Requirements
- Python 3.x
- Required libraries: os, datetime, urllib, xml.etree.ElementTree, csv, argparse

## Examples
See the `examples/` directory for example usage scripts and queries.