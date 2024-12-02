from .plain_text_processor import PlainTextProcessor
from .html_processor import HTMLProcessor
from .markdown_processor import MarkdownProcessor

class ContentProcessor:
    def parse(self, content: str) -> str:
        if content.strip().startswith('<'):
            return HTMLProcessor().parse(content)
        elif content.strip().startswith('#'):
            return MarkdownProcessor().parse(content)
        else:
            return PlainTextProcessor().parse(content)
