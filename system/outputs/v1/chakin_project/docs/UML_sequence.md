sequenceDiagram
    participant User
    participant CLI
    participant Chakin
    participant CSVHandler
    participant ProgressBar
    User->>CLI: Run search command
    CLI->>Chakin: search(lang='English')
    Chakin->>CSVHandler: search_by_language('English')
    CSVHandler-->>Chakin: List of Datasets
    Chakin-->>CLI: Display search results
    User->>CLI: Run download command
    CLI->>Chakin: download(number=2, save_dir='./')
    Chakin->>CSVHandler: load_csv('datasets.csv')
    CSVHandler-->>Chakin: Dataset
    Chakin->>ProgressBar: start()
    Chakin->>ProgressBar: update(progress)
    Chakin->>ProgressBar: finish()
    Chakin-->>CLI: Download complete