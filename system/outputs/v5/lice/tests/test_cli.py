import unittest
from unittest.mock import patch
from src.cli import CLI

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
    def test_executeCommand(self, mock_print, mock_generateLicense):
        args = {'license': 'mit', 'org': 'ExampleOrg', 'year': 2023}
        self.cli.executeCommand(args)
        mock_generateLicense.assert_called_once_with('mit', 2023, 'ExampleOrg')
        mock_print.assert_called_once_with('MIT License Text')

if __name__ == '__main__':
    unittest.main()