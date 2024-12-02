import unittest
import os
import subprocess
from src.query_arxiv import QueryArXiv
from src.utils.command_line_interface import CommandLineInterface

class TestQueryArXivFeatures(unittest.TestCase):
    def setUp(self):
        self.test_csv_file = 'test_results.csv'

    def tearDown(self):
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)

    def test_query_execution_with_console_output(self):
        args = [
            '--category', 'cs.CL',
            '--title', 'neural',
            '--author', 'Smith',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--verbose'
        ]
        cli = CommandLineInterface()
        params = cli.parse_arguments(args)
        query_arxiv = QueryArXiv(**params)
        query_arxiv.executeQuery()
        # This test is visual, ensure it prints correctly to console

    def test_query_execution_with_csv_output(self):
        args = [
            '--category', 'cs.CL',
            '--title', 'neural',
            '--author', 'Smith',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--to_file', self.test_csv_file
        ]
        cli = CommandLineInterface()
        params = cli.parse_arguments(args)
        query_arxiv = QueryArXiv(**params)
        query_arxiv.executeQuery()
        self.assertTrue(os.path.exists(self.test_csv_file))

    def test_query_execution_with_console_and_csv_output(self):
        args = [
            '--category', 'cs.CL',
            '--title', 'neural',
            '--author', 'Smith',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--to_file', self.test_csv_file,
            '--verbose'
        ]
        cli = CommandLineInterface()
        params = cli.parse_arguments(args)
        query_arxiv = QueryArXiv(**params)
        query_arxiv.executeQuery()
        self.assertTrue(os.path.exists(self.test_csv_file))
        # This test is visual, ensure it prints correctly to console

    def test_query_execution_with_missing_required_argument(self):
        args = [
            '--category', 'cs.CL'
        ]
        cli = CommandLineInterface()
        with self.assertRaises(SystemExit):
            cli.parse_arguments(args)

if __name__ == '__main__':
    unittest.main()
