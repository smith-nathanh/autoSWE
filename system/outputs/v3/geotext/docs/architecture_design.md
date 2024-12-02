geotext/
│   README.md
│
├───geotext/
│   ├───__init__.py
│   ├───geotext.py
│   └───data_file/
│       ├───citypatches.txt
│       ├───countryInfo.txt
│       ├───nationalities.txt
│       └───cities15000.txt
│
└───examples/
    ├───demo.py
    └───example_usage.sh

README.md:
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

examples/example_usage.sh:
```bash
#!/bin/bash

# Example usage of GeoText
python -c "from geotext import GeoText; print(GeoText().extract_cities('I visited Paris and Berlin.'))"
python -c "from geotext import GeoText; print(GeoText().extract_countries('I visited France and Germany.'))"
python -c "from geotext import GeoText; print(GeoText().count_country_mentions('France is beautiful. France has great food.'))"
```