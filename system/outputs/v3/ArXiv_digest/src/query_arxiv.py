import argparse
import datetime
import re
from src.api.arxiv_api import ArXivAPI
from src.utils.xml_parser import XMLParser
from src.utils.csv_exporter import CSVExporter

class QueryArXiv:
    def __init__(self):
        self.category = None
        self.title = None
        self.author = None
        self.abstract = None
        self.recent_days = None
        self.to_file = None
        self.verbose = False
        self.max_results = 10

    def execute_query(self):
        self._parse_arguments()
        query_url = self.construct_query_url()
        api = ArXivAPI()
        xml_data = api.fetch_data(query_url)
        parser = XMLParser()
        results = parser.parse(xml_data)
        filtered_results = [result for result in results if self.check_date(result['published'])]
        if self.to_file:
            exporter = CSVExporter()
            exporter.export_to_csv(filtered_results, self.to_file)
        if self.verbose or not self.to_file:
            self.output_results(filtered_results)

    def _parse_arguments(self):
        parser = argparse.ArgumentParser(description='Query ArXiv for research papers.')
        parser.add_argument('--category', type=str, help='Category of the paper.')
        parser.add_argument('--title', type=str, help='Keyword for the title.')
        parser.add_argument('--author', type=str, help='Keyword for the author.')
        parser.add_argument('--abstract', type=str, help='Keyword in the abstract.')
        parser.add_argument('--recent_days', type=int, required=True, help='Filter papers from the most recent k days.')
        parser.add_argument('--to_file', type=str, help='Path to save the results in CSV format.')
        parser.add_argument('--verbose', action='store_true', help='Flag to print results to the console.')
        args = parser.parse_args()

        self.category = args.category
        self.title = args.title
        self.author = args.author
        self.abstract = args.abstract
        self.recent_days = args.recent_days
        self.to_file = args.to_file
        self.verbose = args.verbose

        if not any([self.category, self.title, self.author, self.abstract]):
            raise ValueError('At least one of the query parameters [category, title, author, abstract] must be provided.')

        self._validate_arguments()

    def _validate_arguments(self):
        pattern = re.compile(r'^[A-Za-z0-9+:.]+$')
        for arg in [self.category, self.title, self.author, self.abstract]:
            if arg and not pattern.match(arg):
                raise ValueError('Arguments must be constructed with only characters from "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+:."')

    def construct_query_url(self):
        base_url = "http://export.arxiv.org/api/query?"
        search_query = []
        if self.category:
            search_query.append(f"cat:{self.category}")
        if self.title:
            search_query.append(f"ti:{self.title}")
        if self.author:
            search_query.append(f"au:{self.author}")
        if self.abstract:
            search_query.append(f"abs:{self.abstract}")
        search_query = '+AND+'.join(search_query)
        query_url = f"{base_url}search_query={search_query}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={self.max_results}"
        return query_url

    def check_date(self, published_date):
        published_date = datetime.datetime.strptime(published_date, '%Y-%m-%dT%H:%M:%SZ')
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=self.recent_days)
        return published_date >= cutoff_date

    def output_results(self, results):
        for result in results:
            print(f"Category: {result['category']}")
            print(f"Title: {result['title']}")
            print(f"Author: {result['author']}")
            print(f"Abstract: {result['abstract']}")
            print(f"Published: {result['published']}")
            print(f"Link: {result['link']}")
            print("-" * 40)
