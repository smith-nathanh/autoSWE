classDiagram
    class ReadTimeCalculator {
        +int default_wpm
        +estimate_reading_time(content: str, wpm: int) int
        +process_plain_text(content: str) int
        +process_html(content: str) int
        +process_markdown(content: str) int
    }

    class ContentProcessor {
        +parse(content: str) str
    }

    class PlainTextProcessor {
        +parse(content: str) str
    }

    class HTMLProcessor {
        +parse(content: str) str
    }

    class MarkdownProcessor {
        +parse(content: str) str
    }

    ReadTimeCalculator --> ContentProcessor
    ContentProcessor <|-- PlainTextProcessor
    ContentProcessor <|-- HTMLProcessor
    ContentProcessor <|-- MarkdownProcessor