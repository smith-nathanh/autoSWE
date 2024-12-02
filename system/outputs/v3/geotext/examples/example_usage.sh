#!/bin/bash

# Example usage of GeoText
python -c "from geotext import GeoText; print(GeoText().extract_cities('I visited Paris and Berlin.'))"
python -c "from geotext import GeoText; print(GeoText().extract_countries('I visited France and Germany.'))"
python -c "from geotext import GeoText; print(GeoText().count_country_mentions('France is beautiful. France has great food.'))"