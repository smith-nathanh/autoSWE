import pytest
from src.read_time_calculator import ReadTimeCalculator

class TestReadTimeCalculator:
    def setup_method(self):
        self.calculator = ReadTimeCalculator()

    def test_plain_text_reading_time(self):
        content = "This is a simple test."
        processed_content = self.calculator.process_content(content, 'plain_text')
        reading_time = self.calculator.calculate_reading_time(processed_content)
        assert reading_time == pytest.approx(0.075, 0.01)

    def test_html_reading_time(self):
        content = "<p>This is a simple test.</p>"
        processed_content = self.calculator.process_content(content, 'html')
        reading_time = self.calculator.calculate_reading_time(processed_content)
        assert reading_time == pytest.approx(0.075, 0.01)

    def test_markdown_reading_time(self):
        content = "# Heading\nThis is a simple test."
        processed_content = self.calculator.process_content(content, 'markdown')
        reading_time = self.calculator.calculate_reading_time(processed_content)
        assert reading_time == pytest.approx(0.075, 0.01)

    def test_unsupported_format(self):
        with pytest.raises(ValueError):
            self.calculator.process_content("content", 'unsupported')