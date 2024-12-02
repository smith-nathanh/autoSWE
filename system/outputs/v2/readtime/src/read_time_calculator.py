from content_parser import ContentParser
from error_handler import ErrorHandler

class ReadTimeCalculator:
    def __init__(self):
        self.parser = ContentParser()
        self.error_handler = ErrorHandler()

    def process_content(self, content: str, format: str) -> str:
        self.error_handler.validate_input(content, format)
        if format == 'plain_text':
            return self.parser.parse_plain_text(content)
        elif format == 'html':
            return self.parser.parse_html(content)
        elif format == 'markdown':
            return self.parser.parse_markdown(content)
        else:
            self.error_handler.raise_unsupported_format_error(format)

    def calculate_reading_time(self, content: str, wpm: int = 265) -> float:
        words = content.split()
        num_words = len(words)
        return num_words / wpm

    def handle_error(self, format: str):
        self.error_handler.raise_unsupported_format_error(format)