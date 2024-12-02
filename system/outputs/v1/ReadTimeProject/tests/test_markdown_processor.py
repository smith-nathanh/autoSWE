import pytest
from src.markdown_processor import MarkdownProcessor

@pytest.fixture
def processor():
    return MarkdownProcessor()

def test_parse(processor):
    content = "# Heading\n\nThis is a paragraph."
    assert processor.parse(content).startswith("Heading This is a paragraph.")