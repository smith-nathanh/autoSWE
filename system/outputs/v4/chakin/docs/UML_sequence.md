sequenceDiagram
    participant User
    participant CLI
    participant Chakin
    participant CSVHandler
    participant Dataset
    User->>CLI: Execute search command
    CLI->>Chakin: search(lang)
    Chakin->>CSVHandler: readCSV("./chakin/datasets.csv")
    CSVHandler->>Dataset: Create Dataset instances
    CSVHandler-->>Chakin: Return list of datasets
    Chakin-->>CLI: Return search results
    CLI-->>User: Display search results
    User->>CLI: Execute download command
    CLI->>Chakin: download(number, save_dir)
    Chakin->>CSVHandler: readCSV("./chakin/datasets.csv")
    CSVHandler->>Dataset: Create Dataset instances
    CSVHandler-->>Chakin: Return dataset
    Chakin-->>CLI: Download file with progress bar
    CLI-->>User: Display download progress