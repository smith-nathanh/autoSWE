import unittest
from geotext.geotext import GeoText
from geotext.data_loader import DataLoader

class TestGeoText(unittest.TestCase):
    def setUp(self):
        self.geo_text = GeoText()

    def test_extract_cities(self):
        text = "I have been to New York and Paris."
        cities = self.geo_text.extract_cities(text)
        self.assertIn("New York", cities)
        self.assertIn("Paris", cities)

    def test_extract_cities_empty_text(self):
        text = ""
        cities = self.geo_text.extract_cities(text)
        self.assertEqual(cities, [])

    def test_extract_countries(self):
        text = "I have been to the United States and France."
        countries = self.geo_text.extract_countries(text)
        self.assertIn("United States", countries)
        self.assertIn("France", countries)

    def test_extract_countries_empty_text(self):
        text = ""
        countries = self.geo_text.extract_countries(text)
        self.assertEqual(countries, [])

    def test_filter_cities_by_country(self):
        cities = ["New York", "Paris"]
        filtered_cities = self.geo_text.filter_cities_by_country(cities, "US")
        self.assertIn("New York", filtered_cities)
        self.assertNotIn("Paris", filtered_cities)

    def test_count_country_mentions(self):
        text = "I have been to the United States and France."
        country_mentions = self.geo_text.count_country_mentions(text)
        self.assertEqual(country_mentions.get("United States", 0), 1)
        self.assertEqual(country_mentions.get("France", 0), 1)

    def test_count_country_mentions_empty_text(self):
        text = ""
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
        self.assertIn('AD', country_info)
        self.assertEqual(country_info['AD']['Country'], 'Andorra')

    def test_load_nationalities(self):
        nationalities = self.data_loader.load_nationalities()
        self.assertIn('afghan', nationalities)
        self.assertEqual(nationalities['afghan'], 'AF')

    def test_load_cities(self):
        cities = self.data_loader.load_cities()
        self.assertTrue(any(city['name'] == 'Palikir - National Government Center' for city in cities))

    def test_load_city_patches_invalid_format(self):
        with open('geotext/data_file/citypatches.txt', 'w') as file:
            file.write('invalid_line_without_tab')
        with self.assertRaises(ValueError):
            self.data_loader.load_city_patches()

    def test_load_country_info_missing_key(self):
        with open('geotext/data_file/countryInfo.txt', 'w') as file:
            file.write('ISO3\tISO-Numeric\tfips\tCountry\tCapital\tArea\tPopulation\tContinent\ttld\tCurrencyCode\tCurrencyName\tPhone\tPostal Code Format\tPostal Code Regex\tLanguages\tgeonameid\tneighbours\tEquivalentFipsCode\n')
        with self.assertRaises(KeyError):
            self.data_loader.load_country_info()

if __name__ == '__main__':
    unittest.main()
