import unittest
from geotext.geotext import GeoText

class TestGeoTextFeatures(unittest.TestCase):
    def setUp(self):
        self.geo_text = GeoText()
        self.text = "I have been to New York and Paris."

    def test_city_extraction(self):
        """Test that cities are correctly extracted from text."""
        cities = self.geo_text.extract_cities(self.text)
        self.assertIn("New York", cities, "New York should be extracted as a city.")
        self.assertIn("Paris", cities, "Paris should be extracted as a city.")

    def test_country_extraction(self):
        """Test that countries are correctly extracted from text."""
        countries = self.geo_text.extract_countries(self.text)
        self.assertIn("United States", countries, "United States should be extracted as a country.")
        self.assertIn("France", countries, "France should be extracted as a country.")

    def test_country_mention_count(self):
        """Test that country mentions are correctly counted in text."""
        country_mentions = self.geo_text.count_country_mentions(self.text)
        self.assertEqual(country_mentions.get("United States", 0), 1, "United States should be mentioned once.")
        self.assertEqual(country_mentions.get("France", 0), 1, "France should be mentioned once.")

    def test_filter_cities_by_country(self):
        """Test filtering of cities by country code."""
        cities = self.geo_text.extract_cities(self.text)
        filtered_cities = self.geo_text.filter_cities_by_country(cities, 'US')
        self.assertIn("New York", filtered_cities, "New York should be in the filtered list for US.")
        self.assertNotIn("Paris", filtered_cities, "Paris should not be in the filtered list for US.")

if __name__ == '__main__':
    unittest.main()
