# Financial Data Analysis Program

## Overview
This project is a Python-based financial data analysis tool designed to compute various financial indicators. It processes financial data, calculates indicators, and provides insights for investment decisions.

## Features
- **Financial Data Processing**: Load and preprocess data from CSV files.
- **Indicator Calculations**: Compute Renko, Line Break, and Point and Figure charts.
- **Instrument Analysis**: Analyze stocks and commodities.
- **Reporting**: Generate reports summarizing analysis results.
- **Testing and Validation**: Comprehensive unit and acceptance tests.

## Technical Requirements
- Python 3.x
- Libraries: Pandas, Numpy, Matplotlib, Pytest

## Usage
To generate indicators, run the following script:
```bash
python examples/demo.py
```

## Project Structure
- `examples/`: Example scripts and usage demonstrations.
- `src/`: Source code for data processing, indicator calculations, analysis, and reporting.
- `tests/`: Unit tests for validating functionality.
- `acceptance_samples/`: CSV files for acceptance testing.
- `unit_samples/`: CSV files for unit testing.

## Installation
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib pytest
   ```

## Running Tests
To run all tests, execute:
```bash
pytest tests/
```