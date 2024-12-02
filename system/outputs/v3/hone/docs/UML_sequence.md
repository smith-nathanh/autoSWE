sequenceDiagram
    participant User
    participant CLI
    participant CSVParser
    participant JSONGenerator
    participant Utilities
    User->>CLI: Run conversion command
    CLI->>Utilities: Open CSV file
    Utilities-->>CLI: Return file object
    CLI->>CSVParser: Read CSV file
    CSVParser-->>CLI: Return data
    CLI->>JSONGenerator: Convert data to JSON
    JSONGenerator-->>CLI: Return JSON object
    CLI->>Utilities: Open JSON file
    Utilities-->>CLI: Return file object
    CLI->>JSONGenerator: Output JSON to file
    JSONGenerator-->>CLI: Confirmation
    CLI-->>User: Conversion complete