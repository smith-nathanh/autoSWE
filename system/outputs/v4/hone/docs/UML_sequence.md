sequenceDiagram
    participant User
    participant CLI
    participant CSVParser
    participant JSONGenerator
    participant FileManager

    User->>CLI: Run conversion command
    CLI->>CSVParser: Parse CSV file
    CSVParser->>FileManager: Open CSV file
    FileManager-->>CSVParser: Return file object
    CSVParser->>CSVParser: Extract column names and data rows
    CSVParser->>FileManager: Close CSV file
    CSVParser-->>CLI: Return parsed data
    CLI->>JSONGenerator: Convert data to JSON
    JSONGenerator->>FileManager: Open JSON file
    FileManager-->>JSONGenerator: Return file object
    JSONGenerator->>FileManager: Write JSON data
    JSONGenerator->>FileManager: Close JSON file
    JSONGenerator-->>CLI: Conversion complete
    CLI-->>User: Notify completion