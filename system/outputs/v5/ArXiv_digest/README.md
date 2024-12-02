# Query ArXiv

Query ArXiv is a command-line tool designed to streamline the process of fetching research papers from the ArXiv database. It allows users to perform advanced searches based on parameters like category, author, title, and abstract, with an added feature to filter results based on recent publication dates.

## Features
- Advanced Query Options
- Time-based Filtering
- Output Handling
- User Input Processing
- Data Retrieval and Processing
- Result Filtering and Formatting

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
- Libraries: os, datetime, urllib, xml.etree.ElementTree, csv, and argparse

## Installation
Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd project-root
```

## Running Tests
To run tests, execute the following command from the root directory:

```bash
python -m unittest discover tests
```