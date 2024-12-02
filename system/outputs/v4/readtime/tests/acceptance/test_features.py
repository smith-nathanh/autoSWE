import unittest
from src.read_time_calculator import ReadTimeCalculator

class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()

    def test_estimate_reading_time_plain_text(self):
        with open('samples/plain_text.txt', 'r') as file:
            content = file.read()
            processed_content = self.calculator.process_content(content, 'plain_text')
            reading_time = self.calculator.calculate_reading_time(processed_content)
            self.assertAlmostEqual(reading_time, 0.075, delta=0.01)

    def test_estimate_reading_time_html(self):
        with open('samples/html.html', 'r') as file:
            content = file.read()
            processed_content = self.calculator.process_content(content, 'html')
            reading_time = self.calculator.calculate_reading_time(processed_content)
            self.assertAlmostEqual(reading_time, 0.075, delta=0.01)

    def test_estimate_reading_time_markdown(self):
        with open('samples/markdown.md', 'r') as file:
            content = file.read()
            processed_content = self.calculator.process_content(content, 'markdown')
            reading_time = self.calculator.calculate_reading_time(processed_content)
            self.assertAlmostEqual(reading_time, 0.075, delta=0.01)

    def test_handle_unsupported_format(self):
        with self.assertRaises(ValueError):
            self.calculator.process_content("content", "unsupported")

    def test_default_wpm_rate(self):
        content = "This is a test text with a default WPM rate."
        reading_time = self.calculator.calculate_reading_time(content)
        self.assertAlmostEqual(reading_time, 0.113, delta=0.01)

if __name__ == '__main__':
    unittest.main()