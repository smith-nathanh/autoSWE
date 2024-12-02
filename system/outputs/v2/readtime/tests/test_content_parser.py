import pytest
from src.content_parser import ContentParser

@pytest.fixture
def parser():
    return ContentParser()


def test_parse_plain_text(parser):
    content = "This is a plain text."
    assert parser.parse_plain_text(content) == content


def test_parse_html(parser):
    content = "<p>This is a HTML text.</p>"
    assert parser.parse_html(content) == "This is a HTML text."


def test_parse_markdown(parser):
    content = "# This is a markdown text."
    assert parser.parse_markdown(content) == "This is a markdown text."