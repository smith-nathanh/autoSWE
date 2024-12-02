import unittest
from src.read_time_calculator import ReadTimeCalculator
from src.error_handler import ErrorHandler

class TestReadTimeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()
        self.error_handler = ErrorHandler()

    def test_plain_text_reading_time(self):
        content = "This is a sample plain text file to test reading time estimation."
        expected_time = len(content.split()) / 265
        self.assertAlmostEqual(self.calculator.process_content(content, 'plain_text'), expected_time)

    def test_html_reading_time(self):
        content = "<html><body><p>This is a sample HTML file to test reading time estimation.</p></body></html>"
        expected_time = len("This is a sample HTML file to test reading time estimation.".split()) / 265
        self.assertAlmostEqual(self.calculator.process_content(content, 'html'), expected_time)

    def test_markdown_reading_time(self):
        content = "# Sample Markdown\n\nThis is a sample markdown file to test reading time estimation."
        expected_time = len("Sample Markdown This is a sample markdown file to test reading time estimation.".split()) / 265
        self.assertAlmostEqual(self.calculator.process_content(content, 'markdown'), expected_time)

    def test_unsupported_format(self):
        content = "This is a sample content."
        format = "unsupported_format"
        expected_error = "Error: Unsupported format 'unsupported_format'. Supported formats are plain_text, html, markdown."
        self.assertEqual(self.calculator.process_content(content, format), expected_error)

    def test_empty_content(self):
        with self.assertRaises(ValueError):
            self.error_handler.validate_input("", "plain_text")

    def test_empty_format(self):
        with self.assertRaises(ValueError):
            self.error_handler.validate_input("Some content", "")

if __name__ == '__main__':
    unittest.main()
