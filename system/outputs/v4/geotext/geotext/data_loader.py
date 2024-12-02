import os

class DataLoader:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), 'data_file')

    def load_city_patches(self):
        # Load city patches
        city_patches = {}
        with open(os.path.join(self.data_path, 'citypatches.txt'), 'r') as file:
            for line in file:
                city, country_code = line.strip().split('\t')
                city_patches[city] = country_code
        return city_patches

    def load_country_info(self):
        # Load country info
        country_info = {}
        with open(os.path.join(self.data_path, 'countryInfo.txt'), 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                country_info[parts[4]] = {
                    'iso': parts[0],
                    'iso3': parts[1],
                    'iso_numeric': parts[2],
                    'fips': parts[3],
                    'country': parts[4],
                    'capital': parts[5],
                    'area': int(parts[6]),
                    'population': int(parts[7]),
                    'continent': parts[8],
                    'tld': parts[9],
                    'currency_code': parts[10],
                    'currency_name': parts[11],
                    'phone': parts[12],
                    'postal_code_format': parts[13],
                    'postal_code_regex': parts[14],
                    'languages': parts[15],
                    'geonameid': int(parts[16]),
                    'neighbours': parts[17],
                    'equivalent_fips_code': parts[18]
                }
        return country_info

    def load_nationalities(self):
        # Load nationalities
        nationalities = {}
        with open(os.path.join(self.data_path, 'nationalities.txt'), 'r') as file:
            for line in file:
                nationality, country_code = line.strip().split(':')
                nationalities[nationality] = country_code
        return nationalities

    def load_cities(self):
        # Load cities
        cities = []
        with open(os.path.join(self.data_path, 'cities15000.txt'), 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                cities.append({
                    'geonameid': int(parts[0]),
                    'name': parts[1],
                    'latitude': float(parts[4]),
                    'longitude': float(parts[5]),
                    'feature_class': parts[6],
                    'feature_code': parts[7],
                    'country_code': parts[8],
                    'population': int(parts[14]),
                    'timezone': parts[17],
                    'modification_date': parts[18]
                })
        return cities