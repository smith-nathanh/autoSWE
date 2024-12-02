import unittest
from src.read_time_calculator import ReadTimeCalculator
from src.content_processor import ContentProcessor

class TestAcceptanceFeatures(unittest.TestCase):
    def setUp(self):
        self.calculator = ReadTimeCalculator()
        self.processor = ContentProcessor()

    def test_reading_time_estimation_html(self):
        html_content = """
        <html>
        <head><title>Sample HTML</title></head>
        <body>
            <h1>Welcome to the Sample HTML</h1>
            <p>This is a paragraph in HTML format. It contains some text to estimate reading time.</p>
            <p>Another paragraph with more text to read and calculate the reading time.</p>
        </body>
        </html>
        """
        expected_time = 1  # Assuming default WPM and content length
        reading_time = self.calculator.estimate_reading_time(html_content)
        self.assertEqual(reading_time, expected_time)

    def test_reading_time_estimation_markdown(self):
        markdown_content = """
        # Sample Markdown

        Welcome to the sample markdown file. This file contains some text to estimate reading time.

        ## Subheading

        More text here to provide content for reading time estimation.

        - Bullet point one
        - Bullet point two

        ### Another Subheading

        Even more text to ensure the reading time calculation is accurate.
        """
        expected_time = 1  # Assuming default WPM and content length
        reading_time = self.calculator.estimate_reading_time(markdown_content)
        self.assertEqual(reading_time, expected_time)

    def test_reading_time_estimation_plain_text(self):
        plain_text_content = """
        This is a sample plain text file. It contains simple text to estimate reading time.

        The purpose of this text is to provide content for the reading time calculator to process and estimate how long it would take to read this text based on a given words-per-minute rate.
        """
        expected_time = 1  # Assuming default WPM and content length
        reading_time = self.calculator.estimate_reading_time(plain_text_content)
        self.assertEqual(reading_time, expected_time)

    def test_handling_different_wpm_rates(self):
        content = "Word " * 1000
        expected_time_200_wpm = 5
        expected_time_500_wpm = 2
        reading_time_200_wpm = self.calculator.estimate_reading_time(content, 200)
        reading_time_500_wpm = self.calculator.estimate_reading_time(content, 500)
        self.assertEqual(reading_time_200_wpm, expected_time_200_wpm)
        self.assertEqual(reading_time_500_wpm, expected_time_500_wpm)

    def test_error_handling_unsupported_format(self):
        unsupported_content = "{ 'key': 'value' }"
        with self.assertRaises(Exception):
            self.processor.parse(unsupported_content)

if __name__ == '__main__':
    unittest.main()
