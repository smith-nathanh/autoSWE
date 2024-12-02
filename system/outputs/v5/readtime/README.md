# ReadTime Project

The ReadTime project is a Python-based tool designed to estimate the reading time for various content formats, including plain text, HTML, and markdown. The tool provides users with an approximate reading time based on a standard or user-defined words-per-minute (WPM) rate.

## Features
- Processes plain text, HTML, and markdown content.
- Calculates reading time based on a specified WPM rate (default is 265).
- Handles errors and validates unsupported formats.

## Usage
To estimate reading time, run the following script:
```bash
python examples/demo.py
```

## Project Structure
- `samples/`: Contains sample files for testing.
- `src/`: Contains the source code for the project.
- `tests/`: Contains unit tests for the project.
- `examples/`: Contains example scripts demonstrating usage.

## Dependencies
- Python 3.x
- beautifulsoup4
- lxml
- markdown2
- pytest
- pyquery

## Installation
Install the required dependencies using pip:
```bash
pip install beautifulsoup4 lxml markdown2 pytest pyquery
```

## Running Tests
To run the tests, execute the following command:
```bash
pytest tests/
```