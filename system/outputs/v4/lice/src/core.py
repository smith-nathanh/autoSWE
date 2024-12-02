import sys
from .cli import CLI


def main():
    cli = CLI()
    args = cli.parseArguments(sys.argv[1:])
    cli.executeCommand(args)


if __name__ == "__main__":
    main()