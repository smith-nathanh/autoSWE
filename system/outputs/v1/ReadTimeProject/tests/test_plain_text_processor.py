import pytest
from src.plain_text_processor import PlainTextProcessor

@pytest.fixture
def processor():
    return PlainTextProcessor()

def test_parse(processor):
    content = "   This is a plain text.   "
    assert processor.parse(content) == "This is a plain text."