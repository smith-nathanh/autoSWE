import argparse
import datetime
import re
from src.arxiv_api import ArXivAPI
from src.xml_parser import XMLParser
from src.csv_exporter import CSVExporter

class QueryArXiv:
    def __init__(self, args):
        self.args = self.parse_arguments(args)
        self.api = ArXivAPI()
        self.parser = XMLParser()
        self.exporter = CSVExporter()

    def parse_arguments(self, args):
        parser = argparse.ArgumentParser(description='Query ArXiv for research papers.')
        parser.add_argument('--category', type=str, help='Category of the paper.')
        parser.add_argument('--title', type=str, help='Keyword for the title.')
        parser.add_argument('--author', type=str, help='Keyword for the author.')
        parser.add_argument('--abstract', type=str, help='Keyword in the abstract.')
        parser.add_argument('--recent_days', type=int, required=True, help='Filter papers from the most recent k days.')
        parser.add_argument('--to_file', type=str, help='Path to save the results in CSV format.')
        parser.add_argument('--verbose', action='store_true', help='Flag to print results to the console.')
        return parser.parse_args(args)

    def execute_query(self):
        query_url = self.construct_query_url()
        xml_data = self.api.fetch_data(query_url)
        results = self.parser.parse(xml_data)
        filtered_results = [result for result in results if self.check_date(result['published'])]
        if self.args.to_file:
            self.exporter.export_to_csv(filtered_results, self.args.to_file)
        if self.args.verbose or not self.args.to_file:
            self.output_results(filtered_results)

    def construct_query_url(self):
        base_url = "http://export.arxiv.org/api/query?"
        search_query = []
        if self.args.category:
            search_query.append(f"cat:{self.args.category}")
        if self.args.author:
            search_query.append(f"au:{self.args.author}")
        if self.args.title:
            search_query.append(f"ti:{self.args.title}")
        if self.args.abstract:
            search_query.append(f"abs:{self.args.abstract}")
        if not search_query:
            raise ValueError("At least one of category, author, title, or abstract must be specified.")
        search_query = '+AND+'.join(search_query)
        query_url = f"{base_url}search_query={search_query}&sortBy=submittedDate&sortOrder=descending&start=0&max_results=10"
        return query_url

    def check_date(self, published_date):
        published_date = datetime.datetime.strptime(published_date, "%Y-%m-%dT%H:%M:%SZ")
        recent_days_ago = datetime.datetime.now() - datetime.timedelta(days=self.args.recent_days)
        return published_date >= recent_days_ago

    def output_results(self, results):
        for result in results:
            print(f"Category: {result['category']}")
            print(f"Title: {result['title']}")
            print(f"Author: {result['author']}")
            print(f"Abstract: {result['abstract']}")
            print(f"Published: {result['published']}")
            print(f"Link: {result['link']}")
            print("-")