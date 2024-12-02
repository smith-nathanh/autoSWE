sequenceDiagram
    participant User
    participant CLI
    participant Chakin
    participant CSVHandler
    participant Dataset
    User->>CLI: Execute search command
    CLI->>Chakin: search(lang)
    Chakin->>CSVHandler: loadCSV(filePath)
    CSVHandler->>CSVHandler: parseCSV()
    CSVHandler->>Chakin: Return list of Datasets
    Chakin->>CLI: Display search results
    User->>CLI: Execute download command
    CLI->>Chakin: download(number, save_dir)
    Chakin->>CSVHandler: loadCSV(filePath)
    CSVHandler->>CSVHandler: parseCSV()
    CSVHandler->>Chakin: Return Dataset
    Chakin->>CLI: Show progress bar
    Chakin->>User: Download complete