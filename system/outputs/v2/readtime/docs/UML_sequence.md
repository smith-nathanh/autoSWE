sequenceDiagram
    participant User
    participant ReadTimeCalculator
    participant ContentParser
    participant ErrorHandler
    User->>ReadTimeCalculator: provide content and format
    ReadTimeCalculator->>ContentParser: parse content
    ContentParser-->>ReadTimeCalculator: parsed content
    ReadTimeCalculator->>ReadTimeCalculator: calculate reading time
    alt unsupported format
        ReadTimeCalculator->>ErrorHandler: handle error
        ErrorHandler-->>User: error message
    else supported format
        ReadTimeCalculator-->>User: estimated reading time
    end