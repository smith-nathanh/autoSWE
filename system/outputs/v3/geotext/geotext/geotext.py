import os
import re
from typing import List, Dict

class GeoText:
    def __init__(self):
        self.data_loader = DataFileLoader()
        self.city_patches = self.data_loader.load_city_patches()
        self.countries_info = self.data_loader.load_country_info()
        self.cities = self.data_loader.load_cities()

    def extract_cities(self, text: str) -> List[str]:
        city_mentions = []
        for city in self.cities:
            if city.name in text:
                city_mentions.append(city.name)
        return city_mentions

    def extract_countries(self, text: str) -> List[str]:
        country_mentions = []
        for country in self.countries_info.values():
            if country.country in text:
                country_mentions.append(country.country)
        return country_mentions

    def filter_cities_by_country(self, cities: List[str], country_code: str) -> List[str]:
        filtered_cities = []
        for city in cities:
            for city_obj in self.cities:
                if city_obj.name == city and city_obj.country_code == country_code:
                    filtered_cities.append(city)
        return filtered_cities

    def count_country_mentions(self, text: str) -> Dict[str, int]:
        country_count = {}
        for country in self.countries_info.values():
            count = text.count(country.country)
            if count > 0:
                country_count[country.country] = count
        return country_count

class DataFileLoader:
    DATA_DIR = os.path.join(os.path.dirname(__file__), 'data_file')

    def load_city_patches(self) -> Dict[str, str]:
        city_patches = {}
        with open(os.path.join(self.DATA_DIR, 'citypatches.txt'), 'r') as file:
            for line in file:
                city, country_code = line.strip().split('\t')
                city_patches[city] = country_code
        return city_patches

    def load_country_info(self) -> Dict[str, 'CountryInfo']:
        country_info = {}
        with open(os.path.join(self.DATA_DIR, 'countryInfo.txt'), 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                country = CountryInfo(*parts)
                country_info[country.iso] = country
        return country_info

    def load_nationalities(self) -> Dict[str, str]:
        nationalities = {}
        with open(os.path.join(self.DATA_DIR, 'nationalities.txt'), 'r') as file:
            for line in file:
                nationality, country_code = line.strip().split(':')
                nationalities[nationality] = country_code
        return nationalities

    def load_cities(self) -> List['City']:
        cities = []
        with open(os.path.join(self.DATA_DIR, 'cities15000.txt'), 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                city = City(*parts)
                cities.append(city)
        return cities

class CountryInfo:
    def __init__(self, iso, iso3, iso_numeric, fips, country, capital, area, population, continent, tld, currency_code, currency_name, phone, postal_code_format, postal_code_regex, languages, geonameid, neighbours, equivalent_fips_code):
        self.iso = iso
        self.iso3 = iso3
        self.iso_numeric = iso_numeric
        self.fips = fips
        self.country = country
        self.capital = capital
        self.area = int(area)
        self.population = int(population)
        self.continent = continent
        self.tld = tld
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.phone = phone
        self.postal_code_format = postal_code_format
        self.postal_code_regex = postal_code_regex
        self.languages = languages
        self.geonameid = int(geonameid)
        self.neighbours = neighbours.split(',') if neighbours else []
        self.equivalent_fips_code = equivalent_fips_code

class City:
    def __init__(self, geonameid, name, *args):
        self.geonameid = int(geonameid)
        self.name = name
        self.latitude = float(args[0])
        self.longitude = float(args[1])
        self.feature_class = args[2]
        self.feature_code = args[3]
        self.country_code = args[4]
        self.population = int(args[5])
        self.timezone = args[6]
        self.modification_date = args[7]