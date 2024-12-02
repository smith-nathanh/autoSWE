import unittest
from src.license_generator import LicenseGenerator

class TestLicenseGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = LicenseGenerator()

    def test_generate_license(self):
        license_text = self.generator.generateLicense('mit', 2023, 'ExampleOrg')
        self.assertIn('ExampleOrg', license_text)
        self.assertIn('2023', license_text)

    def test_generate_header(self):
        header_text = self.generator.generateHeader('mit', 'Python')
        self.assertIn('Python', header_text)

    def test_save_to_file(self):
        content = "Sample License"
        filename = "test_license.txt"
        self.generator.saveToFile(content, filename)
        with open(filename, 'r') as file:
            self.assertEqual(file.read(), content)

if __name__ == '__main__':
    unittest.main()