import unittest
from geotext import GeoText

class TestGeoText(unittest.TestCase):
    def setUp(self):
        self.geo_text = GeoText()

    def test_extract_cities(self):
        text = "I visited Paris and Berlin."
        expected_cities = ["Paris", "Berlin"]
        extracted_cities = self.geo_text.extract_cities(text)
        self.assertEqual(extracted_cities, expected_cities)

    def test_extract_countries(self):
        text = "I visited France and Germany."
        expected_countries = ["France", "Germany"]
        extracted_countries = self.geo_text.extract_countries(text)
        self.assertEqual(extracted_countries, expected_countries)

    def test_filter_cities_by_country(self):
        cities = ["Paris", "Berlin", "Munich"]
        country_code = "DE"
        expected_filtered_cities = ["Berlin", "Munich"]
        filtered_cities = self.geo_text.filter_cities_by_country(cities, country_code)
        self.assertEqual(filtered_cities, expected_filtered_cities)

    def test_count_country_mentions(self):
        text = "France is beautiful. Germany is also beautiful. France has great food."
        expected_country_mentions = {"France": 2, "Germany": 1}
        country_mentions = self.geo_text.count_country_mentions(text)
        self.assertEqual(country_mentions, expected_country_mentions)

if __name__ == '__main__':
    unittest.main()
