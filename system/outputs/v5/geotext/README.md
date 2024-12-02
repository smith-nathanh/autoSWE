# GeoText

GeoText is a Python library designed to extract city and country mentions from texts. It provides a simple yet effective solution for geo-location data extraction from various text sources, facilitating tasks in data analysis, geographic information systems, and content tagging.

## Features
- Extract city and country names from text.
- Filter cities by country codes.
- Count mentions of different countries in the text.
- No external dependencies, uses standard Python libraries.
- Supports multiple languages.

## Installation

To install GeoText, clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd project-root
```

## Usage

Run the demo script to see GeoText in action:

```bash
python examples/demo.py
```

## Testing

To run the tests, use:

```bash
pytest tests/
```

## Data Sources

GeoText uses data from [geonames.org](http://www.geonames.org) to identify geographical information.