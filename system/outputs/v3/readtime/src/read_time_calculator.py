from .content_parser import ContentParser
from .error_handler import ErrorHandler

class ReadTimeCalculator:
    def __init__(self):
        self.parser = ContentParser()
        self.error_handler = ErrorHandler()

    def process_content(self, content: str, format: str) -> str:
        try:
            if format == 'plain_text':
                parsed_content = self.parser.parse_plain_text(content)
            elif format == 'html':
                parsed_content = self.parser.parse_html(content)
            elif format == 'markdown':
                parsed_content = self.parser.parse_markdown(content)
            else:
                return self.error_handler.handle_unsupported_format(format)
            return self.calculate_reading_time(parsed_content)
        except Exception as e:
            return str(e)

    def calculate_reading_time(self, content: str, wpm: int = 265) -> float:
        words = content.split()
        num_words = len(words)
        reading_time = num_words / wpm
        return round(reading_time, 2)
