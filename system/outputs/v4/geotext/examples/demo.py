from geotext.geotext import GeoText

def main():
    text = "I have visited Paris and Berlin."
    geo_text = GeoText()

    cities = geo_text.extract_cities(text)
    countries = geo_text.extract_countries(text)
    country_mentions = geo_text.count_country_mentions(text)

    print("Cities:", cities)
    print("Countries:", countries)
    print("Country Mentions:", country_mentions)

if __name__ == "__main__":
    main()