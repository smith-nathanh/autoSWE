import pytest
from src.content_processor import ContentProcessor

@pytest.fixture
def processor():
    return ContentProcessor()

@pytest.mark.parametrize("content, expected_start", [
    ("<html><body>Test</body></html>", "Test"),
    ("# Heading\nContent", "Heading Content"),
    ("Plain text content.", "Plain text content."),
])
def test_parse(processor, content, expected_start):
    parsed_content = processor.parse(content)
    assert parsed_content.startswith(expected_start)
