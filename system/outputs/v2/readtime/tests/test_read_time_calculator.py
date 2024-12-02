import pytest
from src.read_time_calculator import ReadTimeCalculator

@pytest.fixture
def calculator():
    return ReadTimeCalculator()


def test_calculate_reading_time_plain_text(calculator):
    content = "This is a simple plain text."
    reading_time = calculator.calculate_reading_time(content)
    assert reading_time == pytest.approx(0.113, 0.01)


def test_calculate_reading_time_html(calculator):
    content = "<p>This is a simple HTML text.</p>"
    reading_time = calculator.calculate_reading_time(content)
    assert reading_time == pytest.approx(0.113, 0.01)


def test_calculate_reading_time_markdown(calculator):
    content = "# This is a simple markdown text."
    reading_time = calculator.calculate_reading_time(content)
    assert reading_time == pytest.approx(0.113, 0.01)


def test_unsupported_format(calculator):
    with pytest.raises(ValueError, match="Unsupported format: xml"):
        calculator.process_content("<xml></xml>", "xml")