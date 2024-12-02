import unittest
from src.read_time_calculator import ReadTimeCalculator

class TestReadTimeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()
        
    def test_plain_text_reading_time(self):
        with open('samples/plain_text.txt', 'r') as file:
            content = file.read()
        reading_time = self.calculator.process_content(content, 'plain_text')
        self.assertAlmostEqual(float(reading_time), 0.02, places=2)

    def test_html_reading_time(self):
        with open('samples/html.html', 'r') as file:
            content = file.read()
        reading_time = self.calculator.process_content(content, 'html')
        self.assertAlmostEqual(float(reading_time), 0.02, places=2)

    def test_markdown_reading_time(self):
        with open('samples/markdown.md', 'r') as file:
            content = file.read()
        reading_time = self.calculator.process_content(content, 'markdown')
        self.assertAlmostEqual(float(reading_time), 0.02, places=2)

    def test_unsupported_format(self):
        reading_time = self.calculator.process_content("Some content", 'unsupported_format')
        self.assertEqual(reading_time, "Error: Unsupported format 'unsupported_format'. Supported formats are plain_text, html, markdown.")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.calculator.process_content("", '')

if __name__ == '__main__':
    unittest.main()
