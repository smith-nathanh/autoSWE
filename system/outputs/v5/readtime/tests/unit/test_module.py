import unittest
from src.read_time_calculator import ReadTimeCalculator
from src.content_parser import ContentParser
from src.error_handler import ErrorHandler

class TestReadTimeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()

    def test_plain_text_reading_time(self):
        content = "This is a simple test."
        processed_content = self.calculator.process_content(content, 'plain_text')
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.075, delta=0.01)

    def test_html_reading_time(self):
        content = "<p>This is a simple test.</p>"
        processed_content = self.calculator.process_content(content, 'html')
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.075, delta=0.01)

    def test_markdown_reading_time(self):
        content = "# Heading\nThis is a simple test."
        processed_content = self.calculator.process_content(content, 'markdown')
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.075, delta=0.01)

    def test_unsupported_format(self):
        with self.assertRaises(ValueError):
            self.calculator.process_content("content", 'unsupported')

class TestContentParser(unittest.TestCase):
    def setUp(self):
        self.parser = ContentParser()

    def test_parse_plain_text(self):
        content = "This is a test."
        self.assertEqual(self.parser.parse_plain_text(content), content)

    def test_parse_html(self):
        content = "<p>This is a test.</p>"
        self.assertEqual(self.parser.parse_html(content), "This is a test.")

    def test_parse_markdown(self):
        content = "# Heading\nThis is a test."
        self.assertEqual(self.parser.parse_markdown(content), "Heading\nThis is a test.")

class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        self.error_handler = ErrorHandler()

    def test_validate_format_supported(self):
        try:
            self.error_handler.validate_format('plain_text')
        except ValueError:
            self.fail("validate_format raised ValueError unexpectedly!")

    def test_validate_format_unsupported(self):
        with self.assertRaises(ValueError):
            self.error_handler.validate_format('unsupported')

if __name__ == '__main__':
    unittest.main()