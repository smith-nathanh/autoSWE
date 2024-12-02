import csv

class DataLoader:
    def load_city_patches(self):
        city_patches = {}
        with open('geotext/data_file/citypatches.txt', 'r') as file:
            for line in file:
                city, country_code = line.strip().split('\t')
                city_patches[city] = country_code
        return city_patches

    def load_country_info(self):
        country_info = {}
        with open('geotext/data_file/countryInfo.txt', 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                country_info[row['ISO']] = row
        return country_info

    def load_nationalities(self):
        nationalities = {}
        with open('geotext/data_file/nationalities.txt', 'r') as file:
            for line in file:
                nationality, country_code = line.strip().split(':')
                nationalities[nationality] = country_code
        return nationalities

    def load_cities(self):
        cities = []
        with open('geotext/data_file/cities15000.txt', 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                cities.append({'name': row['name'], 'country_code': row['country_code']})
        return cities