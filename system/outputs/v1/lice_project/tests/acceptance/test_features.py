import unittest
import subprocess
import os

class TestLiceFeatures(unittest.TestCase):
    def setUp(self):
        self.license_types = ['bsd3', 'mit', 'gpl3', 'apache', 'bsd2']
        self.test_org = 'ExampleOrg'
        self.test_year = '2021'
        self.test_language = 'py'
        self.test_file = 'LICENSE'

    def test_generate_license(self):
        """Test that licenses are generated without errors and contain correct text."""
        for license_type in self.license_types:
            result = subprocess.run(['python', 'lice_project/core.py', license_type], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertIn('License', result.stdout)

    def test_custom_organization_and_year(self):
        """Test that custom organization and year are reflected in the license."""
        result = subprocess.run(['python', 'lice_project/core.py', 'gpl3', '--year', self.test_year, '--org', self.test_org], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn(self.test_year, result.stdout)
        self.assertIn(self.test_org, result.stdout)

    def test_custom_template(self):
        """Test that a custom template is used when specified."""
        custom_template_path = 'lice_project/templates/template-apache.txt'
        result = subprocess.run(['python', 'lice_project/core.py', 'apache', '--template', custom_template_path], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        with open(custom_template_path, 'r') as template_file:
            template_content = template_file.read()
        self.assertIn(template_content, result.stdout)

    def test_license_formatting_for_language(self):
        """Test that the license is formatted according to the specified programming language."""
        result = subprocess.run(['python', 'lice_project/core.py', 'apache', '--header', '--language', self.test_language], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('#', result.stdout)  # Assuming Python comment style

    def test_output_to_file(self):
        """Test that the license is correctly written to a specified file."""
        result = subprocess.run(['python', 'lice_project/core.py', 'bsd2', '--file', self.test_file], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as file:
            content = file.read()
        self.assertIn('BSD', content)
        os.remove(self.test_file)  # Clean up after test

    def test_list_template_variables(self):
        """Test that the --vars option lists all template variables for a license type."""
        result = subprocess.run(['python', 'lice_project/core.py', 'gpl3', '--vars'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('year', result.stdout)
        self.assertIn('organization', result.stdout)

if __name__ == '__main__':
    unittest.main()
