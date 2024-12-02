from geotext.geotext import GeoText

def main():
    text = "I have been to New York and Paris."
    geo_text = GeoText()
    cities = geo_text.extract_cities(text)
    countries = geo_text.extract_countries(text)
    country_mentions = geo_text.count_country_mentions(text)

    print("Cities found:", cities)
    print("Countries found:", countries)
    print("Country mentions:", country_mentions)

if __name__ == "__main__":
    main()
