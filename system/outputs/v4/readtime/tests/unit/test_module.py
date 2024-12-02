import unittest
from src.read_time_calculator import ReadTimeCalculator
from src.content_parser import ContentParser
from src.error_handler import ErrorHandler

class TestReadTimeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()

    def test_calculate_reading_time_plain_text(self):
        content = "This is a test text."
        reading_time = self.calculator.calculate_reading_time(content)
        self.assertAlmostEqual(reading_time, 0.075, places=2)

    def test_calculate_reading_time_html(self):
        content = "<p>This is a test HTML.</p>"
        processed_content = self.calculator.process_content(content, 'html')
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.075, places=2)

    def test_calculate_reading_time_markdown(self):
        content = "# Test Markdown\nThis is a test markdown."
        processed_content = self.calculator.process_content(content, 'markdown')
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.075, places=2)

    def test_process_content_unsupported_format(self):
        with self.assertRaises(ValueError):
            self.calculator.process_content("content", "unsupported")

class TestContentParser(unittest.TestCase):
    def setUp(self):
        self.parser = ContentParser()

    def test_parse_plain_text(self):
        content = "This is plain text."
        self.assertEqual(self.parser.parse_plain_text(content), content)

    def test_parse_html(self):
        content = "<p>This is HTML.</p>"
        self.assertEqual(self.parser.parse_html(content), "This is HTML.")

    def test_parse_markdown(self):
        content = "# Heading\nThis is markdown."
        self.assertEqual(self.parser.parse_markdown(content), "Heading\nThis is markdown.")

class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        self.handler = ErrorHandler()

    def test_validate_format_supported(self):
        try:
            self.handler.validate_format('plain_text')
        except ValueError:
            self.fail("validate_format raised ValueError unexpectedly!")

    def test_validate_format_unsupported(self):
        with self.assertRaises(ValueError):
            self.handler.validate_format('unsupported')

if __name__ == '__main__':
    unittest.main()
