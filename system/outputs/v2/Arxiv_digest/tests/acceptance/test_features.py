import unittest
import subprocess
import os
import csv
from datetime import datetime, timedelta

class TestQueryArXivFeatures(unittest.TestCase):
    def setUp(self):
        self.script_path = 'query_arxiv.py'
        self.example_csv_path = 'examples/example_query_results.csv'

    def test_successful_query_execution(self):
        """Test successful execution of queries with various combinations of parameters."""
        result = subprocess.run([
            'python', self.script_path,
            '--category', 'cs.CL',
            '--author', 'Smith',
            '--title', 'neural',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--to_file', self.example_csv_path,
            '--verbose'
        ], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Category:', result.stdout)
        self.assertIn('Title:', result.stdout)
        self.assertIn('Author:', result.stdout)
        self.assertIn('Abstract:', result.stdout)
        self.assertIn('Published:', result.stdout)
        self.assertIn('Link:', result.stdout)

    def test_recent_days_filtering(self):
        """Test accurate filtering based on the recent_days parameter."""
        subprocess.run([
            'python', self.script_path,
            '--category', 'cs.CL',
            '--author', 'Smith',
            '--title', 'neural',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--to_file', self.example_csv_path
        ])
        with open(self.example_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                published_date = datetime.strptime(row['published'], "%Y-%m-%d")
                recent_days_ago = datetime.now() - timedelta(days=30)
                self.assertGreaterEqual(published_date, recent_days_ago)

    def test_csv_output_format(self):
        """Test correct formatting and data integrity in CSV file."""
        subprocess.run([
            'python', self.script_path,
            '--category', 'cs.CL',
            '--author', 'Smith',
            '--title', 'neural',
            '--abstract', 'learning',
            '--recent_days', '30',
            '--to_file', self.example_csv_path
        ])
        with open(self.example_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            self.assertEqual(headers, ['category', 'title', 'author', 'abstract', 'published', 'link'])
            for row in reader:
                self.assertIn('cs.CL', row['category'])
                self.assertIsInstance(row['title'], str)
                self.assertIsInstance(row['author'], str)
                self.assertIsInstance(row['abstract'], str)
                self.assertIsInstance(row['published'], str)
                self.assertIsInstance(row['link'], str)

    def tearDown(self):
        if os.path.exists(self.example_csv_path):
            os.remove(self.example_csv_path)

if __name__ == '__main__':
    unittest.main()
