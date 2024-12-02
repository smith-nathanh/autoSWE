import unittest
import subprocess
import os

class TestLiceFeatures(unittest.TestCase):
    def setUp(self):
        # Ensure the templates directory exists
        self.templates_dir = './templates/'
        self.assertTrue(os.path.exists(self.templates_dir), "Templates directory does not exist.")

    def test_generate_bsd3_license(self):
        result = subprocess.run(['python', 'lice/core.py', 'bsd3'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('BSD 3-Clause License', result.stdout)

    def test_generate_mit_license(self):
        result = subprocess.run(['python', 'lice/core.py', 'mit'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('MIT License', result.stdout)

    def test_generate_gpl3_license_with_year_and_org(self):
        result = subprocess.run(['python', 'lice/core.py', 'gpl3', '--year', '2021', '--org', 'ExampleOrg'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('GNU General Public License', result.stdout)
        self.assertIn('2021', result.stdout)
        self.assertIn('ExampleOrg', result.stdout)

    def test_generate_apache_license_with_header(self):
        result = subprocess.run(['python', 'lice/core.py', 'apache', '--header', '--language', 'py'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Apache License', result.stdout)
        self.assertIn('"""', result.stdout)  # Check for Python header format

    def test_generate_bsd2_license_to_file(self):
        output_file = 'LICENSE'
        result = subprocess.run(['python', 'lice/core.py', 'bsd2', '--file', output_file], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(output_file))
        with open(output_file, 'r') as file:
            content = file.read()
            self.assertIn('BSD 2-Clause License', content)
        os.remove(output_file)  # Clean up

    def test_list_template_variables(self):
        result = subprocess.run(['python', 'lice/core.py', 'mit', '--vars'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('year', result.stdout)
        self.assertIn('org', result.stdout)

    def test_generate_custom_license_with_template(self):
        custom_template_path = './templates/custom-template.txt'
        # Create a dummy custom template for testing
        with open(custom_template_path, 'w') as file:
            file.write('Custom License Template for {org} in {year}')

        result = subprocess.run(['python', 'lice/core.py', 'custom', '--template', custom_template_path], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Custom License Template', result.stdout)

        os.remove(custom_template_path)  # Clean up

if __name__ == '__main__':
    unittest.main()
