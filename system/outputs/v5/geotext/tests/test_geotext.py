import unittest
from geotext.geotext import GeoText

class TestGeoText(unittest.TestCase):
    def setUp(self):
        self.geo_text = GeoText()
        self.text = "I have been to New York and Paris."

    def test_extract_cities(self):
        cities = self.geo_text.extract_cities(self.text)
        self.assertIn("New York", cities)
        self.assertIn("Paris", cities)

    def test_extract_countries(self):
        countries = self.geo_text.extract_countries(self.text)
        self.assertIn("United States", countries)
        self.assertIn("France", countries)

    def test_count_country_mentions(self):
        country_mentions = self.geo_text.count_country_mentions(self.text)
        self.assertEqual(country_mentions.get("United States", 0), 1)
        self.assertEqual(country_mentions.get("France", 0), 1)

if __name__ == '__main__':
    unittest.main()
