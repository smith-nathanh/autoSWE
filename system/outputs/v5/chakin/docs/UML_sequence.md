sequenceDiagram
    participant User
    participant CLI
    participant Chakin
    participant DatasetManager
    participant ProgressBar
    User->>CLI: Run search command
    CLI->>Chakin: search(lang='English')
    Chakin->>DatasetManager: getVectorsByLanguage('English')
    DatasetManager-->>Chakin: List of WordVectors
    Chakin-->>CLI: Display list of WordVectors
    User->>CLI: Run download command
    CLI->>Chakin: download(number=2, save_dir='./')
    Chakin->>DatasetManager: loadDatasets('datasets.csv')
    DatasetManager-->>Chakin: List of WordVectors
    Chakin->>ProgressBar: start()
    loop Downloading
        Chakin->>ProgressBar: update(progress)
    end
    Chakin->>ProgressBar: finish()
    Chakin-->>CLI: Download complete