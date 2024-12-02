from geotext import GeoText

def main():
    text = "I visited Paris and Berlin. France is beautiful."
    geo = GeoText()

    cities = geo.extract_cities(text)
    print(f"Cities mentioned: {cities}")

    countries = geo.extract_countries(text)
    print(f"Countries mentioned: {countries}")

    country_mentions = geo.count_country_mentions(text)
    print(f"Country mentions: {country_mentions}")

if __name__ == "__main__":
    main()