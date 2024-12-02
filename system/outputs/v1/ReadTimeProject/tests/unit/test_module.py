import unittest
from src.read_time_calculator import ReadTimeCalculator
from src.content_processor import ContentProcessor
from src.plain_text_processor import PlainTextProcessor
from src.html_processor import HTMLProcessor
from src.markdown_processor import MarkdownProcessor

class TestReadTimeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()

    def test_estimate_reading_time_default_wpm(self):
        content = "This is a test."
        expected = 1  # 4 words, default WPM is 265, should return 1 minute
        self.assertEqual(self.calculator.estimate_reading_time(content), expected)

    def test_estimate_reading_time_custom_wpm(self):
        content = "Word " * 1000  # 1000 words
        expected = 5  # 1000 words at 200 WPM should take 5 minutes
        self.assertEqual(self.calculator.estimate_reading_time(content, 200), expected)

class TestContentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ContentProcessor()

    def test_parse_html_content(self):
        content = "<html><body>Test</body></html>"
        expected_start = "Test"
        self.assertTrue(self.processor.parse(content).startswith(expected_start))

    def test_parse_markdown_content(self):
        content = "# Heading\nContent"
        expected_start = "Heading Content"
        self.assertTrue(self.processor.parse(content).startswith(expected_start))

    def test_parse_plain_text_content(self):
        content = "Plain text content."
        expected = "Plain text content."
        self.assertEqual(self.processor.parse(content), expected)

class TestPlainTextProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PlainTextProcessor()

    def test_parse(self):
        content = "   This is a plain text.   "
        expected = "This is a plain text."
        self.assertEqual(self.processor.parse(content), expected)

class TestHTMLProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = HTMLProcessor()

    def test_parse(self):
        content = "<html><body><p>This is a paragraph.</p></body></html>"
        expected = "This is a paragraph."
        self.assertEqual(self.processor.parse(content), expected)

class TestMarkdownProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = MarkdownProcessor()

    def test_parse(self):
        content = "# Heading\n\nThis is a paragraph."
        expected_start = "Heading This is a paragraph."
        self.assertTrue(self.processor.parse(content).startswith(expected_start))

if __name__ == '__main__':
    unittest.main()
