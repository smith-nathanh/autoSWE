import unittest
from geotext import GeoText

class TestGeoText(unittest.TestCase):
    def setUp(self):
        self.geo = GeoText()

    def test_extract_cities(self):
        text = "I visited Paris and Berlin."
        expected_cities = ['Paris', 'Berlin']
        self.assertEqual(self.geo.extract_cities(text), expected_cities)

    def test_extract_countries(self):
        text = "I visited France and Germany."
        expected_countries = ['France', 'Germany']
        self.assertEqual(self.geo.extract_countries(text), expected_countries)

    def test_count_country_mentions(self):
        text = "France is beautiful. France has great food."
        expected_count = {'France': 2}
        self.assertEqual(self.geo.count_country_mentions(text), expected_count)

    def test_filter_cities_by_country(self):
        cities = ['Paris', 'Berlin', 'Munich']
        country_code = 'DE'
        expected_filtered_cities = ['Berlin', 'Munich']
        self.assertEqual(self.geo.filter_cities_by_country(cities, country_code), expected_filtered_cities)

    def test_load_city_patches(self):
        city_patches = self.geo.data_loader.load_city_patches()
        self.assertIn('oklahoma', city_patches)
        self.assertEqual(city_patches['oklahoma'], 'US')

    def test_load_country_info(self):
        countries_info = self.geo.data_loader.load_country_info()
        self.assertIn('AD', countries_info)
        self.assertEqual(countries_info['AD'].country, 'Andorra')

    def test_load_nationalities(self):
        nationalities = self.geo.data_loader.load_nationalities()
        self.assertIn('afghan', nationalities)
        self.assertEqual(nationalities['afghan'], 'AF')

    def test_load_cities(self):
        cities = self.geo.data_loader.load_cities()
        city_names = [city.name for city in cities]
        self.assertIn('Palikir - National Government Center', city_names)

if __name__ == '__main__':
    unittest.main()
