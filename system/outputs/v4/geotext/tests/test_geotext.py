import unittest
from geotext.geotext import GeoText

class TestGeoText(unittest.TestCase):
    def setUp(self):
        self.geo_text = GeoText()
        self.text = "I have visited Paris and Berlin."

    def test_extract_cities(self):
        cities = self.geo_text.extract_cities(self.text)
        self.assertIn("Paris", cities)
        self.assertIn("Berlin", cities)

    def test_extract_countries(self):
        countries = self.geo_text.extract_countries(self.text)
        self.assertIn("France", countries)
        self.assertIn("Germany", countries)

    def test_count_country_mentions(self):
        country_mentions = self.geo_text.count_country_mentions(self.text)
        self.assertEqual(country_mentions.get("France"), 1)
        self.assertEqual(country_mentions.get("Germany"), 1)

if __name__ == '__main__':
    unittest.main()