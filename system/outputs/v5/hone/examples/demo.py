import os
import sys

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from cli import CLI

if __name__ == '__main__':
    cli = CLI()
    args = cli.parse_arguments()
    cli.execute_conversion(args)