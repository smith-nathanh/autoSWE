import pytest
from src.html_processor import HTMLProcessor

@pytest.fixture
def processor():
    return HTMLProcessor()

def test_parse(processor):
    content = "<html><body><p>This is a paragraph.</p></body></html>"
    assert processor.parse(content) == "This is a paragraph."