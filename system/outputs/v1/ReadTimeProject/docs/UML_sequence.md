sequenceDiagram
    participant User
    participant DemoScript
    participant ReadTimeCalculator
    participant ContentProcessor
    participant PlainTextProcessor
    participant HTMLProcessor
    participant MarkdownProcessor

    User->>DemoScript: Run demo.py
    DemoScript->>ReadTimeCalculator: estimate_reading_time(content, wpm)
    ReadTimeCalculator->>ContentProcessor: parse(content)
    alt Plain Text
        ContentProcessor->>PlainTextProcessor: parse(content)
        PlainTextProcessor-->>ContentProcessor: parsed content
    else HTML
        ContentProcessor->>HTMLProcessor: parse(content)
        HTMLProcessor-->>ContentProcessor: parsed content
    else Markdown
        ContentProcessor->>MarkdownProcessor: parse(content)
        MarkdownProcessor-->>ContentProcessor: parsed content
    end
    ContentProcessor-->>ReadTimeCalculator: parsed content
    ReadTimeCalculator-->>DemoScript: estimated reading time
    DemoScript-->>User: Display reading time