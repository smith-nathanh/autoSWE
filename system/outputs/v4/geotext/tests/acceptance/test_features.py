import unittest
from geotext.geotext import GeoText

class TestGeoTextFeatures(unittest.TestCase):
    def setUp(self):
        self.geo_text = GeoText()

    def test_city_and_country_extraction(self):
        text = "I have visited Paris and Berlin."
        cities = self.geo_text.extract_cities(text)
        countries = self.geo_text.extract_countries(text)
        self.assertIn("Paris", cities)
        self.assertIn("Berlin", cities)
        self.assertIn("France", countries)
        self.assertIn("Germany", countries)

    def test_country_code_filtering(self):
        text = "I have visited Paris and Berlin."
        cities = self.geo_text.extract_cities(text)
        filtered_cities = self.geo_text.filter_cities_by_country(cities, 'FR')
        self.assertIn("Paris", filtered_cities)
        self.assertNotIn("Berlin", filtered_cities)

    def test_country_mention_counting(self):
        text = "France is beautiful. Germany is also beautiful. France has great food."
        country_mentions = self.geo_text.count_country_mentions(text)
        self.assertEqual(country_mentions.get("France"), 2)
        self.assertEqual(country_mentions.get("Germany"), 1)

    def test_no_external_dependencies(self):
        # This test is more of a check to ensure no external imports are used
        # beyond standard Python libraries. This is a placeholder for manual review.
        pass

    def test_data_from_reputable_sources(self):
        # This test is a placeholder to ensure data is sourced from geonames.org
        # Actual verification would require manual data source validation.
        pass

    def test_support_for_multiple_languages(self):
        text = "He visitado París y Berlín."
        cities = self.geo_text.extract_cities(text)
        self.assertIn("París", cities)
        self.assertIn("Berlín", cities)

if __name__ == '__main__':
    unittest.main()
