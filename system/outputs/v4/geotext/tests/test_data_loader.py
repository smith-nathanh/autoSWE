import unittest
from geotext.data_loader import DataLoader

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

if __name__ == '__main__':
    unittest.main()