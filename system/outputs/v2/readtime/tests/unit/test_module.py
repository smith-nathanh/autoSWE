import unittest
from src.read_time_calculator import ReadTimeCalculator
from src.content_parser import ContentParser
from src.error_handler import ErrorHandler

class TestReadTimeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()

    def test_calculate_reading_time_plain_text(self):
        content = "This is a simple plain text."
        reading_time = self.calculator.calculate_reading_time(content)
        self.assertAlmostEqual(reading_time, 0.113, places=2)

    def test_calculate_reading_time_html(self):
        content = "<p>This is a simple HTML text.</p>"
        processed_content = self.calculator.process_content(content, "html")
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.113, places=2)

    def test_calculate_reading_time_markdown(self):
        content = "# This is a simple markdown text."
        processed_content = self.calculator.process_content(content, "markdown")
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.113, places=2)

    def test_unsupported_format(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.process_content("<xml></xml>", "xml")
        self.assertEqual(str(context.exception), "Unsupported format: xml")

class TestContentParser(unittest.TestCase):
    def setUp(self):
        self.parser = ContentParser()

    def test_parse_plain_text(self):
        content = "This is a plain text."
        self.assertEqual(self.parser.parse_plain_text(content), content)

    def test_parse_html(self):
        content = "<p>This is a HTML text.</p>"
        self.assertEqual(self.parser.parse_html(content), "This is a HTML text.")

    def test_parse_markdown(self):
        content = "# This is a markdown text."
        self.assertEqual(self.parser.parse_markdown(content), "This is a markdown text.")

class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        self.error_handler = ErrorHandler()

    def test_validate_input(self):
        with self.assertRaises(ValueError) as context:
            self.error_handler.validate_input("", "plain_text")
        self.assertEqual(str(context.exception), "Content and format must be provided.")

    def test_raise_unsupported_format_error(self):
        with self.assertRaises(ValueError) as context:
            self.error_handler.raise_unsupported_format_error("xml")
        self.assertEqual(str(context.exception), "Unsupported format: xml")

if __name__ == '__main__':
    unittest.main()
