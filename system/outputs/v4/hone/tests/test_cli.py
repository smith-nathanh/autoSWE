import unittest
from unittest.mock import patch
from src.cli import CLI

class TestCLI(unittest.TestCase):
    @patch('src.cli.argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(csv_filepath='data_file/comma_test/dataset.csv',
                                           json_filepath='data_file/comma_test/output.json',
                                           delimiters=',',
                                           schema=None))
    def test_parse_arguments(self, mock_args):
        cli = CLI()
        args = cli.parse_arguments()
        self.assertEqual(args['csv_filepath'], 'data_file/comma_test/dataset.csv')
        self.assertEqual(args['json_filepath'], 'data_file/comma_test/output.json')
        self.assertEqual(args['delimiters'], ',')
        self.assertIsNone(args['schema'])

if __name__ == '__main__':
    unittest.main()
