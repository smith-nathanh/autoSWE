import unittest
from geotext.geotext import GeoText
from geotext.data_loader import DataLoader

class TestGeoText(unittest.TestCase):
    def setUp(self):
        self.geo_text = GeoText()

    def test_extract_cities(self):
        text = "I have visited Paris and Berlin."
        cities = self.geo_text.extract_cities(text)
        self.assertIn("Paris", cities)
        self.assertIn("Berlin", cities)

    def test_extract_cities_empty_text(self):
        text = ""
        cities = self.geo_text.extract_cities(text)
        self.assertEqual(cities, [])

    def test_extract_countries(self):
        text = "I have visited France and Germany."
        countries = self.geo_text.extract_countries(text)
        self.assertIn("France", countries)
        self.assertIn("Germany", countries)

    def test_extract_countries_empty_text(self):
        text = ""
        countries = self.geo_text.extract_countries(text)
        self.assertEqual(countries, [])

    def test_filter_cities_by_country(self):
        cities = [
            {'name': 'Paris', 'country_code': 'FR'},
            {'name': 'Berlin', 'country_code': 'DE'}
        ]
        filtered_cities = self.geo_text.filter_cities_by_country(cities, 'FR')
        self.assertEqual(len(filtered_cities), 1)
        self.assertEqual(filtered_cities[0]['name'], 'Paris')

    def test_count_country_mentions(self):
        text = "France is beautiful. France has great food."
        country_mentions = self.geo_text.count_country_mentions(text)
        self.assertEqual(country_mentions.get("France"), 2)

    def test_count_country_mentions_no_mentions(self):
        text = "No countries mentioned here."
        country_mentions = self.geo_text.count_country_mentions(text)
        self.assertEqual(country_mentions, {})

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader()

    def test_load_city_patches(self):
        city_patches = self.data_loader.load_city_patches()
        self.assertIn('oklahoma', city_patches)
        self.assertEqual(city_patches['oklahoma'], 'US')

    def test_load_country_info(self):
        country_info = self.data_loader.load_country_info()
        self.assertIn('Andorra', country_info)
        self.assertEqual(country_info['Andorra']['iso'], 'AD')

    def test_load_nationalities(self):
        nationalities = self.data_loader.load_nationalities()
        self.assertIn('afghan', nationalities)
        self.assertEqual(nationalities['afghan'], 'AF')

    def test_load_cities(self):
        cities = self.data_loader.load_cities()
        self.assertTrue(any(city['name'] == 'Palikir - National Government Center' for city in cities))

    def test_load_cities_invalid_data(self):
        # Simulate invalid data handling
        with self.assertRaises(ValueError):
            self.data_loader.load_cities()

if __name__ == '__main__':
    unittest.main()
