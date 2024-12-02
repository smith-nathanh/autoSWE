project-root/
│   README.md
│
├───samples/
│   │   html.html
│   │   markdown.md
│   │   plain_text.txt
│
├───src/
│   │   read_time_calculator.py
│   │   content_parser.py
│   │   error_handler.py
│
├───tests/
│   │   test_read_time_calculator.py
│   │   test_content_parser.py
│   │   test_error_handler.py
│
└───examples/
    │   demo.py
    │   example_usage.sh
    │   example_html.html
    │   example_markdown.md
    │   example_plain_text.txt

README.md content:
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