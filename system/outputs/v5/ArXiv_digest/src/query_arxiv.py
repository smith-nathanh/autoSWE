import argparse
from datetime import datetime, timedelta
from src.utils.api_interaction import fetch_data
from src.utils.xml_parser import parse_xml_data
from src.utils.date_filter import filter_by_date
from src.utils.output_handler import output_results

class QueryArXiv:
    def __init__(self, category=None, title=None, author=None, abstract=None, recent_days=7, to_file=None, verbose=False):
        self.category = category
        self.title = title
        self.author = author
        self.abstract = abstract
        self.recent_days = recent_days
        self.to_file = to_file
        self.verbose = verbose

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
        query = "+AND+".join(search_query)
        url = f"{base_url}search_query={query}&sortBy=submittedDate&sortOrder=descending&start=0&max_results=10"
        return url

    def execute_query(self):
        url = self.construct_query_url()
        xml_data = fetch_data(url)
        papers = parse_xml_data(xml_data)
        recent_papers = filter_by_date(papers, self.recent_days)
        output_results(recent_papers, self.to_file, self.verbose)


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
        parser.error('At least one of --category, --title, --author, or --abstract must be specified.')

    query_arxiv = QueryArXiv(
        category=args.category,
        title=args.title,
        author=args.author,
        abstract=args.abstract,
        recent_days=args.recent_days,
        to_file=args.to_file,
        verbose=args.verbose
    )
    query_arxiv.execute_query()


if __name__ == "__main__":
    main()
