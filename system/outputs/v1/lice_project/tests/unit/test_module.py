import unittest
from lice_project.core import Lice
from lice_project.cli import CommandLineInterface
from lice_project.environment import Environment

class TestLice(unittest.TestCase):
    def setUp(self):
        self.lice = Lice()

    def test_generateLicense(self):
        # Test generating a BSD3 license
        result = self.lice.generateLicense('bsd3', 2023, 'ExampleOrg', 'py', 'LICENSE')
        self.assertIsNotNone(result)
        # Add more assertions to check the content of the result

    def test_customTemplate(self):
        # Test using a custom template
        result = self.lice.customTemplate('path/to/custom/template.txt')
        self.assertIsNotNone(result)
        # Add more assertions to check the content of the result

    def test_listTemplateVariables(self):
        # Test listing template variables for a specific license type
        variables = self.lice.listTemplateVariables('mit')
        self.assertIsInstance(variables, list)
        self.assertGreater(len(variables), 0)

class TestCommandLineInterface(unittest.TestCase):
    def setUp(self):
        self.cli = CommandLineInterface()

    def test_parseArguments(self):
        # Test parsing command line arguments
        args = ['bsd3', '--year', '2023', '--org', 'ExampleOrg']
        parsed_args = self.cli.parseArguments(args)
        self.assertIsNotNone(parsed_args)
        # Add more assertions to check the parsed arguments

    def test_executeCommand(self):
        # Test executing a command
        self.cli.parseArguments(['bsd3', '--year', '2023', '--org', 'ExampleOrg'])
        result = self.cli.executeCommand()
        self.assertIsNotNone(result)
        # Add more assertions to check the result of the command execution

class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.env = Environment()

    def test_getDefaultOrg(self):
        # Test getting the default organization
        org = self.env.getDefaultOrg()
        self.assertIsNotNone(org)
        # Add more assertions to check the default organization

    def test_getDefaultYear(self):
        # Test getting the default year
        year = self.env.getDefaultYear()
        self.assertIsNotNone(year)
        # Add more assertions to check the default year

if __name__ == '__main__':
    unittest.main()
