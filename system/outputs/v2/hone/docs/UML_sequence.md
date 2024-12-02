sequenceDiagram
    participant User
    participant CLI
    participant CSVParser
    participant JSONGenerator
    participant Utilities
    User->>CLI: Run conversion command
    CLI->>CSVParser: Parse CSV file
    CSVParser->>Utilities: Open CSV file
    Utilities-->>CSVParser: Return file object
    CSVParser->>CSVParser: Extract column names and data rows
    CSVParser-->>CLI: Return parsed data
    CLI->>JSONGenerator: Convert data to JSON
    JSONGenerator->>JSONGenerator: Apply schema
    JSONGenerator->>Utilities: Open JSON file
    Utilities-->>JSONGenerator: Return file object
    JSONGenerator->>Utilities: Write JSON data
    Utilities-->>User: JSON file created