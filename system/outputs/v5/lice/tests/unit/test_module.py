
import unittest
from unittest.mock import patch, mock_open
from src.core import main
from src.license_generator import LicenseGenerator
from src.template_manager import TemplateManager
from src.language_detector import LanguageDetector
from src.cli import CLI
import sys
import os

class TestCore(unittest.TestCase):
    @patch('src.cli.CLI.executeCommand')
    @patch('src.cli.CLI.parseArguments', return_value={'license': 'mit', 'org': 'ExampleOrg', 'year': 2023})
    def test_main(self, mock_parseArguments, mock_executeCommand):
        with patch('sys.argv', ['core.py', 'mit']):
            main()
        mock_parseArguments.assert_called_once()
        mock_executeCommand.assert_called_once()

class TestLicenseGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = LicenseGenerator()

    def test_generateLicense_valid(self):
        license_text = self.generator.generateLicense('mit', 2023, 'ExampleOrg')
        self.assertIn('ExampleOrg', license_text)
        self.assertIn('2023', license_text)

    def test_generateLicense_invalid(self):
        with self.assertRaises(FileNotFoundError):
            self.generator.generateLicense('nonexistent', 2023, 'ExampleOrg')

    def test_generateHeader_valid(self):
        header_text = self.generator.generateHeader('mit', 'Python')
        self.assertIn('Python', header_text)

    def test_generateHeader_invalid(self):
        with self.assertRaises(FileNotFoundError):
            self.generator.generateHeader('nonexistent', 'Python')

    def test_saveToFile(self):
        content = "Sample License Text"
        filename = "test_license.txt"
        self.generator.saveToFile(content, filename)
        with open(filename, 'r') as file:
            self.assertEqual(file.read(), content)
        os.remove(filename)

class TestTemplateManager(unittest.TestCase):
    def setUp(self):
        self.manager = TemplateManager()

    def test_loadTemplate_valid(self):
        template = self.manager.loadTemplate('mit')
        self.assertIn('MIT License', template)

    def test_loadTemplate_invalid(self):
        with self.assertRaises(FileNotFoundError):
            self.manager.loadTemplate('nonexistent')

    def test_listTemplateVariables(self):
        variables = self.manager.listTemplateVariables('mit')
        self.assertIn('year', variables)
        self.assertIn('organization', variables)

class TestLanguageDetector(unittest.TestCase):
    def setUp(self):
        self.detector = LanguageDetector()

    def test_detectLanguage_known(self):
        self.assertEqual(self.detector.detectLanguage('main.py'), 'Python')
        self.assertEqual(self.detector.detectLanguage('index.html'), 'HTML')

    def test_detectLanguage_unknown(self):
        self.assertEqual(self.detector.detectLanguage('unknown.xyz'), 'Unknown')

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(license='mit', org='ExampleOrg', year=2023))
    def test_parseArguments(self, mock_parse_args):
        args = self.cli.parseArguments(['mit', '-o', 'ExampleOrg', '-y', '2023'])
        self.assertEqual(args['license'], 'mit')
        self.assertEqual(args['org'], 'ExampleOrg')
        self.assertEqual(args['year'], 2023)

    @patch('src.license_generator.LicenseGenerator.generateLicense', return_value='MIT License Text')
    @patch('builtins.print')
    def test_executeCommand_valid(self, mock_print, mock_generateLicense):
        args = {'license': 'mit', 'org': 'ExampleOrg', 'year': 2023}
        self.cli.executeCommand(args)
        mock_generateLicense.assert_called_once_with('mit', 2023, 'ExampleOrg')
        mock_print.assert_called_once_with('MIT License Text')

    @patch('builtins.print')
    def test_executeCommand_vars(self, mock_print):
        args = {'license': 'mit', 'vars': True}
        self.cli.executeCommand(args)
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()
