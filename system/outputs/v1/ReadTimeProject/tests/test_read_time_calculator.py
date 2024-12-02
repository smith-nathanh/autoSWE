import pytest
from src.read_time_calculator import ReadTimeCalculator

@pytest.fixture
def calculator():
    return ReadTimeCalculator()

@pytest.mark.parametrize("content, wpm, expected", [
    ("This is a test.", 200, 1),
    ("This is a longer test with more words to read.", 200, 1),
    ("Word " * 1000, 200, 5),
])
def test_estimate_reading_time(calculator, content, wpm, expected):
    assert calculator.estimate_reading_time(content, wpm) == expected
