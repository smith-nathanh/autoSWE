# ReadTime Project

This project is a Python-based tool designed to estimate the reading time for various content formats, including plain text, HTML, and markdown. It allows users to input content and receive an estimated reading time based on a standard or user-defined words-per-minute (WPM) rate.

## Features
- Process and parse plain text, HTML, and markdown content.
- Calculate reading time with a default WPM of 265, adjustable by the user.
- Handle errors for unsupported formats and invalid inputs.

## Usage
To estimate reading time, run the following script:
```
python examples/demo.py
```

## Dependencies
- beautifulsoup4
- lxml
- markdown2
- pytest
- pyquery

## Installation
To install the required dependencies, run:
```
pip install -r requirements.txt
```

## Testing
To run tests, use:
```
pytest
```
