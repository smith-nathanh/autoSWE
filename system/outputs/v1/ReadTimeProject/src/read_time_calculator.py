from .content_processor import ContentProcessor

class ReadTimeCalculator:
    default_wpm = 265

    def estimate_reading_time(self, content: str, wpm: int = None) -> int:
        if wpm is None:
            wpm = self.default_wpm
        processor = ContentProcessor()
        parsed_content = processor.parse(content)
        word_count = len(parsed_content.split())
        return max(1, word_count // wpm)
