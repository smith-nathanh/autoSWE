# demo.py

from hone.cli import CLI

def main():
    cli = CLI()
    args = cli.parse_arguments()
    cli.execute_conversion(args)

if __name__ == '__main__':
    main()