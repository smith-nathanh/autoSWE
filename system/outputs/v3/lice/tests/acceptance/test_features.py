import unittest
import subprocess
import os

class TestLiceFeatures(unittest.TestCase):
    def setUp(self):
        # Ensure the environment is clean before each test
        self.license_file = 'LICENSE'
        if os.path.exists(self.license_file):
            os.remove(self.license_file)

    def test_generate_bsd3_license(self):
        result = subprocess.run(['python', 'lice/core.py', 'bsd3'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Redistribution and use in source and binary forms', result.stdout)

    def test_generate_mit_license(self):
        result = subprocess.run(['python', 'lice/core.py', 'mit'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Permission is hereby granted, free of charge', result.stdout)

    def test_generate_gpl3_license_with_year_and_org(self):
        result = subprocess.run(['python', 'lice/core.py', 'gpl3', '--year', '2021', '--org', 'ExampleOrg'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('2021 ExampleOrg', result.stdout)

    def test_generate_apache_license_with_header(self):
        result = subprocess.run(['python', 'lice/core.py', 'apache', '--header', '--language', 'py'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('# License Header for Python', result.stdout)
        self.assertIn('Licensed under the Apache License, Version 2.0', result.stdout)

    def test_generate_bsd2_license_to_file(self):
        result = subprocess.run(['python', 'lice/core.py', 'bsd2', '--file', self.license_file], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(self.license_file))
        with open(self.license_file, 'r') as f:
            content = f.read()
            self.assertIn('Redistribution and use in source and binary forms', content)

    def test_list_template_vars(self):
        result = subprocess.run(['python', 'lice/core.py', 'list-vars', 'gpl3'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('year', result.stdout)
        self.assertIn('organization', result.stdout)

    def tearDown(self):
        # Clean up any files created during tests
        if os.path.exists(self.license_file):
            os.remove(self.license_file)

if __name__ == '__main__':
    unittest.main()
