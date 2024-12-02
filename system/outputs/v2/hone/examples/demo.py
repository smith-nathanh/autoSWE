import sys
from hone.cli import CLI

def main(args):
    cli = CLI()
    parsed_args = cli.parse_arguments(args)
    cli.execute_conversion(parsed_args)

if __name__ == "__main__":
    main(sys.argv[1:])
