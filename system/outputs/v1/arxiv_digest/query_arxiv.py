import argparse
from arxiv_api import ArXivAPI
from xml_parser import XMLParser
from csv_exporter import CSVExporter
from utils.date_utils import check_date

class QueryArXiv:
    def __init__(self, category, title, author, abstract, recent_days, max_results=10, verbose=False, to_file=None):
        self.category = category
        self.title = title
        self.author = author
        self.abstract = abstract
        self.recent_days = recent_days
        self.max_results = max_results
        self.verbose = verbose
        self.to_file = to_file

    def execute_query(self):
        api = ArXivAPI()
        url = api.construct_query_url(self.category, self.title, self.author, self.abstract, self.max_results)
        data = api.fetch_data(url)

        parser = XMLParser()
        results = parser.parse_xml(data)

        filtered_results = self.filter_results_by_date(results)
        self.output_results(filtered_results)

    def filter_results_by_date(self, results):
        return [result for result in results if check_date(result['published'], self.recent_days)]

    def output_results(self, results):
        if self.verbose or not self.to_file:
            for result in results:
                print(f"Category: {result['category']}")
                print(f"Title: {result['title']}")
                print(f"Author: {result['author']}")
                print(f"Abstract: {result['abstract']}")
                print(f"Published: {result['published']}")
                print(f"Link: {result['link']}")
                print("-" * 40)

        if self.to_file:
            exporter = CSVExporter()
            exporter.export_to_csv(results, self.to_file)


def main():
    parser = argparse.ArgumentParser(description='Query ArXiv for research papers.')
    parser.add_argument('--category', type=str, help='Category of the paper.')
    parser.add_argument('--title', type=str, help='Keyword for the title.')
    parser.add_argument('--author', type=str, help='Keyword for the author.')
    parser.add_argument('--abstract', type=str, help='Keyword in the abstract.')
    parser.add_argument('--recent_days', type=int, required=True, help='Filter papers from the most recent k days.')
    parser.add_argument('--to_file', type=str, help='Path to save the results in CSV format.')
    parser.add_argument('--verbose', action='store_true', help='Flag to print results to the console.')

    args = parser.parse_args()

    if not any([args.category, args.title, args.author, args.abstract]):
        raise ValueError('At least one of the query parameters [category, title, author, abstract] must be provided.')

    query = QueryArXiv(
        category=args.category,
        title=args.title,
        author=args.author,
        abstract=args.abstract,
        recent_days=args.recent_days,
        verbose=args.verbose,
        to_file=args.to_file
    )
    query.execute_query()

if __name__ == '__main__':
    main()
