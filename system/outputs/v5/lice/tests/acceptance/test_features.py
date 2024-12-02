import unittest
from unittest.mock import patch, mock_open
from src.cli import CLI
from src.license_generator import LicenseGenerator
from src.template_manager import TemplateManager

class TestAcceptanceFeatures(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()
        self.generator = LicenseGenerator()
        self.template_manager = TemplateManager()

    @patch('builtins.print')
    def test_generate_license_text(self, mock_print):
        # Test generating a license text
        args = {'license': 'mit', 'org': 'ExampleOrg', 'year': 2023}
        self.cli.executeCommand(args)
        mock_print.assert_called_once()
        self.assertIn('MIT License', mock_print.call_args[0][0])
        self.assertIn('ExampleOrg', mock_print.call_args[0][0])
        self.assertIn('2023', mock_print.call_args[0][0])

    @patch('builtins.print')
    def test_generate_license_with_custom_template(self, mock_print):
        # Test generating a license with a custom template
        custom_template = "Custom License for {{organization}} in {{year}}"
        with patch('builtins.open', mock_open(read_data=custom_template)):
            args = {'license': 'custom', 'org': 'CustomOrg', 'year': 2023, 'template': 'custom_template.txt'}
            self.cli.executeCommand(args)
            mock_print.assert_called_once_with('Custom License for CustomOrg in 2023')

    @patch('builtins.print')
    def test_list_template_variables(self, mock_print):
        # Test listing template variables
        args = {'license': 'mit', 'vars': True}
        self.cli.executeCommand(args)
        mock_print.assert_called_once()
        self.assertIn('year', mock_print.call_args[0][0])
        self.assertIn('organization', mock_print.call_args[0][0])

    @patch('src.license_generator.LicenseGenerator.saveToFile')
    def test_save_license_to_file(self, mock_saveToFile):
        # Test saving license to a file
        args = {'license': 'mit', 'org': 'ExampleOrg', 'year': 2023, 'file': 'LICENSE'}
        self.cli.executeCommand(args)
        mock_saveToFile.assert_called_once()
        self.assertIn('MIT License', mock_saveToFile.call_args[0][0])
        self.assertEqual(mock_saveToFile.call_args[0][1], 'LICENSE')

    @patch('builtins.print')
    def test_generate_license_with_header(self, mock_print):
        # Test generating a license with a header for a specific language
        args = {'license': 'mit', 'org': 'ExampleOrg', 'year': 2023, 'language': 'Python'}
        self.cli.executeCommand(args)
        mock_print.assert_called_once()
        self.assertIn('Python', mock_print.call_args[0][0])
        self.assertIn('MIT License', mock_print.call_args[0][0])

if __name__ == '__main__':
    unittest.main()
