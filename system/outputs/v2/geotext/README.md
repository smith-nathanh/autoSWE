# GeoText

GeoText is a Python library designed to extract city and country mentions from texts. It provides a simple yet effective solution for geo-location data extraction from various text sources, facilitating tasks in data analysis, geographic information systems, and content tagging.

## Features
- **City and Country Extraction**: Extract city and country names from text.
- **Country Code Filtering**: Filter extracted cities by country codes.
- **Country Mention Counting**: Count the number of mentions of different countries in the text.
- **No External Dependencies**: Runs with standard Python libraries.
- **Data from Reputable Sources**: Utilizes geographical data from trusted sources like geonames.org.
- **Support for Multiple Languages**: Recognizes city and country names in various languages.

## Installation

To install GeoText, clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd geotext
```

## Usage

```bash
# Run the demo
python examples/demo.py 
```

## Requirements
- Python 3.x
- Wheel library

## Data
GeoText uses data files located in the `./geotext/data_file` directory:
- `citypatches.txt`
- `countryInfo.txt`
- `nationalities.txt`
- `cities15000.txt`

## License
This project is licensed under the MIT License.