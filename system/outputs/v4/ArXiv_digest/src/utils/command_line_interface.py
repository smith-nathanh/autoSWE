import argparse

class CommandLineInterface:
    def parse_arguments(self, args):
        parser = argparse.ArgumentParser(description='Query ArXiv for research papers.')
        parser.add_argument('--category', type=str, help='Category of the paper.')
        parser.add_argument('--title', type=str, help='Keyword for the title.')
        parser.add_argument('--author', type=str, help='Keyword for the author.')
        parser.add_argument('--abstract', type=str, help='Keyword in the abstract.')
        parser.add_argument('--recent_days', type=int, required=True, help='Filter papers from the most recent k days.')
        parser.add_argument('--to_file', type=str, help='Path to save the results in CSV format.')
        parser.add_argument('--verbose', action='store_true', help='Flag to print results to the console.')
        parsed_args = parser.parse_args(args)

        if not (parsed_args.category or parsed_args.title or parsed_args.author or parsed_args.abstract):
            parser.error('At least one of --category, --title, --author, or --abstract must be specified.')

        return vars(parsed_args)
