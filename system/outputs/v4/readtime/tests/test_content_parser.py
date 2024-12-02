from src.content_parser import ContentParser

class TestContentParser:
    def setup_method(self):
        self.parser = ContentParser()

    def test_parse_plain_text(self):
        content = "This is plain text."
        assert self.parser.parse_plain_text(content) == content

    def test_parse_html(self):
        content = "<p>This is HTML.</p>"
        assert self.parser.parse_html(content) == "This is HTML."

    def test_parse_markdown(self):
        content = "# Heading\nThis is markdown."
        assert self.parser.parse_markdown(content) == "Heading\nThis is markdown."