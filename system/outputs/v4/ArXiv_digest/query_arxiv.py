import sys
from src.query_arxiv import QueryArXiv
from src.utils.command_line_interface import CommandLineInterface

def main(args):
    cli = CommandLineInterface()
    params = cli.parse_arguments(args)
    query_arxiv = QueryArXiv(**params)
    query_arxiv.executeQuery()

if __name__ == "__main__":
    main(sys.argv[1:])
