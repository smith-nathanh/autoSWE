import unittest
from unittest.mock import patch, mock_open
from lice.core import Lice
from lice.license_template import LicenseTemplateContent

class TestLice(unittest.TestCase):
    def setUp(self):
        self.lice = Lice()

    @patch('lice.license_template.open', new_callable=mock_open, read_data='{{ year }} {{ organization }}')
    def test_generate_license_with_defaults(self, mock_file):
        with patch('lice.git_config.GitConfig.get_user_info', return_value={'organization': 'DefaultOrg', 'year': '2023'}):
            with patch('sys.stdout') as mock_stdout:
                self.lice.generate_license('bsd3')
                mock_file.assert_called_with('templates/template-bsd3.txt', 'r')
                self.assertIn('2023 DefaultOrg', mock_stdout.getvalue())

    @patch('lice.license_template.open', new_callable=mock_open, read_data='{{ year }} {{ organization }}')
    def test_generate_license_with_custom_year_and_org(self, mock_file):
        with patch('sys.stdout') as mock_stdout:
            self.lice.generate_license('gpl3', year='2021', org='ExampleOrg')
            mock_file.assert_called_with('templates/template-gpl3.txt', 'r')
            self.assertIn('2021 ExampleOrg', mock_stdout.getvalue())

    @patch('lice.license_template.open', new_callable=mock_open, read_data='{{ year }} {{ organization }}')
    def test_generate_license_with_header(self, mock_file):
        with patch('sys.stdout') as mock_stdout:
            self.lice.generate_license('apache', language='py')
            mock_file.assert_called_with('templates/template-apache.txt', 'r')
            self.assertIn('# License Header for Python', mock_stdout.getvalue())

    @patch('lice.license_template.open', new_callable=mock_open, read_data='{{ year }} {{ organization }}')
    def test_generate_license_to_file(self, mock_file):
        with patch('builtins.open', mock_open()) as mock_output_file:
            self.lice.generate_license('bsd2', file='LICENSE')
            mock_file.assert_called_with('templates/template-bsd2.txt', 'r')
            mock_output_file.assert_called_with('LICENSE', 'w')
            mock_output_file().write.assert_called_once_with('2023 DefaultOrg')

    @patch('lice.license_template.open', new_callable=mock_open, read_data='{{ year }} {{ organization }}')
    def test_list_template_vars(self, mock_file):
        vars = self.lice.list_template_vars('agpl3')
        mock_file.assert_called_with('templates/template-agpl3.txt', 'r')
        self.assertEqual(vars, ['year', 'organization'])

class TestLicenseTemplateContent(unittest.TestCase):
    def test_apply_variables(self):
        content = LicenseTemplateContent('{{ year }} {{ organization }}')
        result = content.apply_variables({'year': '2023', 'organization': 'TestOrg'})
        self.assertEqual(result, '2023 TestOrg')

    def test_list_variables(self):
        content = LicenseTemplateContent('{{ year }} {{ organization }}')
        vars = content.list_variables()
        self.assertEqual(vars, ['year', 'organization'])

if __name__ == '__main__':
    unittest.main()
