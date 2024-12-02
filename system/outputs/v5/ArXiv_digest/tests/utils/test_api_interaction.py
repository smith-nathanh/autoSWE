import unittest
from unittest.mock import patch
from src.utils.api_interaction import fetch_data

class TestApiInteraction(unittest.TestCase):
    @patch('src.utils.api_interaction.urllib.request.urlopen')
    def test_fetch_data(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = b'<xml>data</xml>'
        result = fetch_data('http://example.com')
        self.assertEqual(result, b'<xml>data</xml>')

if __name__ == '__main__':
    unittest.main()
