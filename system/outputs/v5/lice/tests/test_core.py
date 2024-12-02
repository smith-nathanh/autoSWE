import unittest
from unittest.mock import patch
from src.core import main

class TestCore(unittest.TestCase):
    @patch('src.cli.CLI.executeCommand')
    @patch('src.cli.CLI.parseArguments', return_value={})
    def test_main(self, mock_parseArguments, mock_executeCommand):
        with patch('sys.argv', ['core.py', 'mit']):
            main()
        mock_parseArguments.assert_called_once()
        mock_executeCommand.assert_called_once()

if __name__ == '__main__':
    unittest.main()