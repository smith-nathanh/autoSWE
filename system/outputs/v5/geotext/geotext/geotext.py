from .data_loader import DataLoader

class GeoText:
    def __init__(self):
        self.data_loader = DataLoader()
        self.city_patches = self.data_loader.load_city_patches()
        self.cities_data = self.data_loader.load_cities()
        self.country_info = self.data_loader.load_country_info()

    def extract_cities(self, text: str):
        cities = []
        for city in self.cities_data:
            if city['name'].lower() in text.lower():
                cities.append(city['name'])
        return cities

    def extract_countries(self, text: str):
        countries = []
        for country in self.country_info.values():
            if country['Country'].lower() in text.lower():
                countries.append(country['Country'])
        return countries

    def filter_cities_by_country(self, cities, country_code):
        return [city for city in cities if city in self.city_patches and self.city_patches[city] == country_code]

    def count_country_mentions(self, text: str):
        country_counts = {}
        for country in self.country_info.values():
            count = text.lower().count(country['Country'].lower())
            if count > 0:
                country_counts[country['Country']] = count
        return country_counts