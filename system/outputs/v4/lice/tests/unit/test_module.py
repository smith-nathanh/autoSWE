import unittest
from unittest.mock import patch, mock_open
from src.core import main
from src.license_generator import LicenseGenerator
from src.template_manager import TemplateManager
from src.language_detector import LanguageDetector
from src.cli import CLI
import os

class TestCore(unittest.TestCase):
    def test_main(self):
        with patch('sys.argv', ['core.py', 'mit', '-o', 'ExampleOrg', '-y', '2023']):
            with patch('builtins.print') as mocked_print:
                main()
                mocked_print.assert_called()

class TestLicenseGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = LicenseGenerator()

    def test_generate_license_valid(self):
        license_text = self.generator.generateLicense('mit', 2023, 'ExampleOrg')
        self.assertIn('ExampleOrg', license_text)
        self.assertIn('2023', license_text)

    def test_generate_license_invalid(self):
        with self.assertRaises(FileNotFoundError):
            self.generator.generateLicense('nonexistent', 2023, 'ExampleOrg')

    def test_generate_header_valid(self):
        header_text = self.generator.generateHeader('apache', 'Python')
        self.assertIn('Python', header_text)

    def test_generate_header_invalid(self):
        with self.assertRaises(FileNotFoundError):
            self.generator.generateHeader('nonexistent', 'Python')

    def test_save_to_file(self):
        content = "Sample License"
        filename = "test_license.txt"
        self.generator.saveToFile(content, filename)
        with open(filename, 'r') as file:
            self.assertEqual(file.read(), content)
        os.remove(filename)

class TestTemplateManager(unittest.TestCase):
    def setUp(self):
        self.manager = TemplateManager()

    def test_load_template_valid(self):
        template = self.manager.loadTemplate('mit')
        self.assertIn('{{year}}', template)

    def test_load_template_invalid(self):
        with self.assertRaises(FileNotFoundError):
            self.manager.loadTemplate('nonexistent')

    def test_list_template_variables(self):
        variables = self.manager.listTemplateVariables('mit')
        self.assertIn('year', variables)
        self.assertIn('organization', variables)

class TestLanguageDetector(unittest.TestCase):
    def setUp(self):
        self.detector = LanguageDetector()

    def test_detect_language_known(self):
        language = self.detector.detectLanguage('example.py')
        self.assertEqual(language, 'Python')

    def test_detect_language_unknown(self):
        language = self.detector.detectLanguage('unknown.ext')
        self.assertEqual(language, 'Unknown')

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()

    def test_parse_arguments_valid(self):
        args = self.cli.parseArguments(['mit', '-o', 'ExampleOrg', '-y', '2023'])
        self.assertEqual(args['license'], 'mit')
        self.assertEqual(args['org'], 'ExampleOrg')
        self.assertEqual(args['year'], 2023)

    def test_parse_arguments_invalid(self):
        with self.assertRaises(SystemExit):
            self.cli.parseArguments([])

    def test_execute_command_vars(self):
        with patch('builtins.print') as mocked_print:
            self.cli.executeCommand({'license': 'mit', 'vars': True})
            mocked_print.assert_called_with('Template variables:', ['year', 'organization'])

    def test_execute_command_generate(self):
        with patch('builtins.print') as mocked_print:
            self.cli.executeCommand({'license': 'mit', 'year': 2023, 'org': 'ExampleOrg'})
            mocked_print.assert_called()

if __name__ == '__main__':
    unittest.main()
