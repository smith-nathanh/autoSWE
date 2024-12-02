# GeoText
GeoText is a Python library designed to extract city and country mentions from texts. It provides functionalities for geo-location data extraction, facilitating tasks in data analysis, geographic information systems, and content tagging.

## Features
- Extract city and country names from text
- Filter cities by country codes
- Count mentions of countries
- No external dependencies
- Supports multiple languages

## Usage
Run the demo using:
```bash
python examples/demo.py
```

## Installation
To install GeoText, clone the repository and navigate to the root directory. Then, run:
```bash
pip install .
```

## Data Files
GeoText uses data files located in the `geotext/data_file` directory. These files include city patches, country information, nationalities, and a list of cities with a population greater than 15,000.

## License
GeoText is licensed under the MIT License.