classDiagram
    class ReadTimeCalculator {
        +process_content(content: str, format: str) str
        +calculate_reading_time(content: str, wpm: int=265) float
        +handle_error(format: str)
    }
    class ContentParser {
        +parse_plain_text(content: str) str
        +parse_html(content: str) str
        +parse_markdown(content: str) str
    }
    class ErrorHandler {
        +validate_format(format: str)
        +handle_unsupported_format(format: str)
    }
    ReadTimeCalculator --> ContentParser : uses
    ReadTimeCalculator --> ErrorHandler : uses