# ReadTime Project

The ReadTime project is a Python-based tool designed to estimate the reading time for various content formats, including plain text, HTML, and markdown. It provides users with an approximate reading time based on a standard or user-defined words-per-minute (WPM) rate.

## Features
- Processes plain text, HTML, and markdown content.
- Calculates reading time based on a specified WPM rate, defaulting to 265 WPM.
- Handles errors and validates unsupported formats.

## Installation

To install the necessary dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To estimate reading time, run the following script:

```
python examples/demo.py
```

## Project Structure

```
project-root/
├── README.md
├── samples/
│   ├── html.html
│   ├── markdown.md
│   └── plain_text.txt
├── src/
│   ├── __init__.py
│   ├── read_time_calculator.py
│   ├── content_parser.py
│   └── error_handler.py
├── tests/
│   ├── __init__.py
│   ├── test_read_time_calculator.py
│   ├── test_content_parser.py
│   └── test_error_handler.py
└── examples/
    ├── demo.py
    └── example_usage.sh
```

## Acceptance Criteria
- Correctly estimates reading time for different content formats.
- Handles different WPM rates, including the default rate.
- Provides proper error handling and messages for unsupported formats.