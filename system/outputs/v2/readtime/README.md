# ReadTime Project

This project is a Python-based tool designed to estimate the reading time for various content formats, including plain text, HTML, and markdown. It calculates reading time based on a standard or user-defined words-per-minute (WPM) rate.

## Features
- Processes plain text, HTML, and markdown content.
- Calculates reading time using a default WPM rate of 265, with options for user-defined rates.
- Handles errors for unsupported formats and validates input.

## Usage
To estimate reading time, run the following script:
```
python examples/demo.py
```

## Dependencies
- Python 3.x
- beautifulsoup4
- lxml
- markdown2
- pytest
- pyquery

## Testing
Test cases are provided in the `tests` directory and can be run using pytest.