project-root/
│   README.md
│   query_arxiv.py
│
├───examples/
│       example_usage.sh
│
└───src/
    │   __init__.py
    │   query_arxiv.py
    │
    ├───utils/
    │       __init__.py
    │       xml_parser.py
    │       csv_exporter.py
    │
    └───api/
            __init__.py
            arxiv_api.py

# README.md
#
# Query ArXiv
#
# Overview
# Query ArXiv is a Python-based tool designed to streamline the process of fetching research papers from the ArXiv database. It allows users to perform advanced searches based on parameters like category, author, title, and abstract, with an added feature to filter results based on recent publication dates.
#
# Features
# - Advanced query options with flexible parameters.
# - Time-based filtering to fetch recent papers.
# - Output options for console and CSV file.
#
# Usage
# To execute a query, run the following script:
# ```bash
# python query_arxiv.py --category [category] --title [title] --author [author] --abstract [abstract] --recent_days [number_of_days] [--to_file path_to_csv_file] [--verbose]
# ```
#
# At least one of the query parameters `[category, title, author, abstract]` must be provided, along with the mandatory `--recent_days` parameter.

# example_usage.sh
#
# Example usage of the Query ArXiv tool
#
# Fetch papers in the category 'cs.CL' by author 'Smith' with 'neural' in the title and 'learning' in the abstract, from the last 7 days, and save to 'results.csv'.
# ```bash
# python query_arxiv.py --category cs.CL --author Smith --title neural --abstract learning --recent_days 7 --to_file results.csv --verbose
# ```