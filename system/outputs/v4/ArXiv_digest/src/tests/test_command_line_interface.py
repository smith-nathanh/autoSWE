import unittest
from src.utils.command_line_interface import CommandLineInterface

class TestCommandLineInterface(unittest.TestCase):
    def test_parse_arguments(self):
        cli = CommandLineInterface()
        args = [
            '--category', 'cs.CL',
            '--title', 'neural',
            '--author', 'Smith',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--to_file', 'results.csv',
            '--verbose'
        ]
        parsed_args = cli.parse_arguments(args)
        self.assertEqual(parsed_args['category'], 'cs.CL')
        self.assertEqual(parsed_args['title'], 'neural')
        self.assertEqual(parsed_args['author'], 'Smith')
        self.assertEqual(parsed_args['abstract'], 'learning')
        self.assertEqual(parsed_args['recent_days'], 30)
        self.assertEqual(parsed_args['to_file'], 'results.csv')
        self.assertTrue(parsed_args['verbose'])

    def test_missing_required_argument(self):
        cli = CommandLineInterface()
        args = ['--category', 'cs.CL']
        with self.assertRaises(SystemExit):
            cli.parse_arguments(args)

if __name__ == '__main__':
    unittest.main()
