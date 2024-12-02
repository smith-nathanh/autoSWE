import unittest
import subprocess
import os

class TestLiceFeatures(unittest.TestCase):
    def setUp(self):
        self.license_types = ['bsd3', 'mit', 'gpl3', 'apache', 'bsd2']
        self.test_org = 'ExampleOrg'
        self.test_year = 2023
        self.test_file = 'test_LICENSE'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_generate_license(self):
        for license_type in self.license_types:
            result = subprocess.run(
                ['python', 'src/core.py', license_type, '-o', self.test_org, '-y', str(self.test_year)],
                capture_output=True, text=True
            )
            self.assertEqual(result.returncode, 0)
            self.assertIn(self.test_org, result.stdout)
            self.assertIn(str(self.test_year), result.stdout)

    def test_generate_license_with_file(self):
        for license_type in self.license_types:
            result = subprocess.run(
                ['python', 'src/core.py', license_type, '-o', self.test_org, '-y', str(self.test_year), '-f', self.test_file],
                capture_output=True, text=True
            )
            self.assertEqual(result.returncode, 0)
            with open(self.test_file, 'r') as file:
                content = file.read()
                self.assertIn(self.test_org, content)
                self.assertIn(str(self.test_year), content)

    def test_generate_license_with_header(self):
        result = subprocess.run(
            ['python', 'src/core.py', 'apache', '-o', self.test_org, '-y', str(self.test_year), '--header', '--language', 'py'],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn(self.test_org, result.stdout)
        self.assertIn(str(self.test_year), result.stdout)
        self.assertIn('Python', result.stdout)

    def test_list_template_variables(self):
        result = subprocess.run(
            ['python', 'src/core.py', 'mit', '--vars'],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn('year', result.stdout)
        self.assertIn('organization', result.stdout)

if __name__ == '__main__':
    unittest.main()
