# Query ArXiv

Query ArXiv is a command-line tool designed to streamline the process of fetching research papers from the ArXiv database. It allows users to perform advanced searches based on parameters like category, author, title, and abstract, with an added feature to filter results based on recent publication dates.

## Features
- Advanced Query Options
- Time-based Filtering
- Output Handling
- User Input Processing
- Data Retrieval and Processing
- Result Filtering and Formatting

## Installation
Ensure you have Python 3.x installed along with the following libraries:
- os
- datetime
- urllib
- xml.etree.ElementTree
- csv
- argparse

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

## Command Line Arguments
- `category` (str, optional): Category of the paper.
- `title` (str, optional): Keyword for the title.
- `author` (str, optional): Keyword for the author.
- `abstract` (str, optional): Keyword in the abstract.
- `recent_days` (int, required): Filter papers from the most recent k days.
- `to_file` (str, optional): Path to save the results in CSV format.
- `verbose` (Boolean, optional): Flag to print results to the console.

## Example
Refer to `examples/example_usage.sh` for example usage.

## License
MIT License