import unittest
from src.read_time_calculator import ReadTimeCalculator

class TestReadTimeCalculatorFeatures(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()

    def test_estimate_reading_time_plain_text(self):
        content = "This is a simple plain text example."
        processed_content = self.calculator.process_content(content, "plain_text")
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.151, places=2)

    def test_estimate_reading_time_html(self):
        content = "<p>This is a simple HTML example.</p>"
        processed_content = self.calculator.process_content(content, "html")
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.151, places=2)

    def test_estimate_reading_time_markdown(self):
        content = "# This is a simple markdown example."
        processed_content = self.calculator.process_content(content, "markdown")
        reading_time = self.calculator.calculate_reading_time(processed_content)
        self.assertAlmostEqual(reading_time, 0.151, places=2)

    def test_handle_different_wpm_rate(self):
        content = "This is a simple plain text example."
        processed_content = self.calculator.process_content(content, "plain_text")
        reading_time = self.calculator.calculate_reading_time(processed_content, wpm=200)
        self.assertAlmostEqual(reading_time, 0.20, places=2)

    def test_error_handling_unsupported_format(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.process_content("<xml></xml>", "xml")
        self.assertEqual(str(context.exception), "Unsupported format: xml")

    def test_error_handling_missing_content_or_format(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.process_content("", "plain_text")
        self.assertEqual(str(context.exception), "Content and format must be provided.")

if __name__ == '__main__':
    unittest.main()
