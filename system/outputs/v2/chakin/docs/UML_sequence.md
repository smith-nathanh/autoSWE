sequenceDiagram
    participant User
    participant CLI
    participant Chakin
    participant CSVHandler
    participant Dataset
    User->>CLI: Execute search command
    CLI->>Chakin: search(lang)
    Chakin->>CSVHandler: loadCSV("./chakin/datasets.csv")
    CSVHandler->>Dataset: Parse CSV
    Dataset-->>CSVHandler: Return list of datasets
    CSVHandler-->>Chakin: Return list of datasets
    Chakin-->>CLI: Return search results
    CLI-->>User: Display search results
    User->>CLI: Execute download command
    CLI->>Chakin: download(number, save_dir)
    Chakin->>CSVHandler: loadCSV("./chakin/datasets.csv")
    CSVHandler->>Dataset: Parse CSV
    Dataset-->>CSVHandler: Return list of datasets
    CSVHandler-->>Chakin: Return dataset info
    Chakin->>CLI: Start download with progress bar
    CLI-->>User: Display download progress