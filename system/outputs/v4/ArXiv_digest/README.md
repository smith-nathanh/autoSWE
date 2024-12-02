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
