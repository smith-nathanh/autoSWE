import unittest
from unittest.mock import patch, mock_open
from lice.license_generator import LicenseGenerator
from lice.template_manager import TemplateManager
from lice.file_manager import FileManager
from lice.config_manager import ConfigManager

class TestLicenseGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = LicenseGenerator()

    @patch('lice.template_manager.TemplateManager.loadTemplate')
    @patch('lice.file_manager.FileManager.createFile')
    def test_generate_license_with_defaults(self, mock_create_file, mock_load_template):
        mock_load_template.return_value = "{year} {org} License"
        self.generator.generateLicense('mit', [])
        mock_create_file.assert_not_called()

    @patch('lice.template_manager.TemplateManager.loadTemplate')
    @patch('lice.file_manager.FileManager.createFile')
    def test_generate_license_with_options(self, mock_create_file, mock_load_template):
        mock_load_template.return_value = "{year} {org} License"
        self.generator.generateLicense('gpl3', ['--year', '2021', '--org', 'ExampleOrg', '--file', 'LICENSE'])
        mock_create_file.assert_called_once_with('LICENSE', '2021 ExampleOrg License')

    @patch('lice.template_manager.TemplateManager.loadTemplate')
    def test_list_template_variables(self, mock_load_template):
        mock_load_template.return_value = "{year} {org} License"
        with patch('builtins.print') as mocked_print:
            self.generator.listTemplateVariables('mit')
            mocked_print.assert_called_once_with('Template variables:', ['year', 'org'])

class TestTemplateManager(unittest.TestCase):
    def setUp(self):
        self.template_manager = TemplateManager()

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data="{year} {org} License")
    def test_load_template(self, mock_open, mock_exists):
        template = self.template_manager.loadTemplate('mit')
        self.assertEqual(template, "{year} {org} License")

    def test_get_template_variables(self):
        template = "{year} {org} License"
        variables = self.template_manager.getTemplateVariables(template)
        self.assertEqual(variables, ['year', 'org'])

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager()

    @patch('builtins.open', new_callable=mock_open)
    def test_create_file(self, mock_open):
        self.file_manager.createFile('LICENSE', 'content')
        mock_open.assert_called_once_with('LICENSE', 'w')
        mock_open().write.assert_called_once_with('content')

    def test_format_header_python(self):
        content = "License Content"
        formatted = self.file_manager.formatHeader(content, 'Python')
        self.assertEqual(formatted, '"""\nLicense Content\n"""')

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.config_manager = ConfigManager()

    @patch('os.getenv', return_value='TestOrg')
    def test_get_default_org(self, mock_getenv):
        org = self.config_manager.getDefaultOrg()
        self.assertEqual(org, 'TestOrg')

    @patch('lice.config_manager.datetime')
    def test_get_default_year(self, mock_datetime):
        mock_datetime.now.return_value.year = 2023
        year = self.config_manager.getDefaultYear()
        self.assertEqual(year, 2023)

if __name__ == '__main__':
    unittest.main()
