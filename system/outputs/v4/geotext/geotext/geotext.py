from .data_loader import DataLoader

class GeoText:
    def __init__(self):
        self.data_loader = DataLoader()
        self.city_patches = self.data_loader.load_city_patches()
        self.cities = self.data_loader.load_cities()
        self.country_info = self.data_loader.load_country_info()

    def extract_cities(self, text: str):
        # Extract cities from text
        extracted_cities = []
        for city in self.cities:
            if city['name'].lower() in text.lower():
                extracted_cities.append(city['name'])
        return extracted_cities

    def extract_countries(self, text: str):
        # Extract countries from text
        extracted_countries = []
        for country in self.country_info.values():
            if country['country'].lower() in text.lower():
                extracted_countries.append(country['country'])
        return extracted_countries

    def filter_cities_by_country(self, cities, country_code):
        # Filter cities by country code
        return [city for city in cities if city['country_code'] == country_code]

    def count_country_mentions(self, text: str):
        # Count country mentions in text
        country_mentions = {}
        for country in self.country_info.values():
            count = text.lower().count(country['country'].lower())
            if count > 0:
                country_mentions[country['country']] = count
        return country_mentions