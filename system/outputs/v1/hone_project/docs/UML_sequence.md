sequenceDiagram
    participant User
    participant CLI
    participant CSVParser
    participant JSONGenerator
    participant FileManager
    User->>CLI: Run conversion command
    CLI->>CLI: parse_arguments()
    CLI->>CSVParser: read_csv(filepath, delimiter)
    CSVParser->>FileManager: open_file(filepath, 'r')
    FileManager-->>CSVParser: file
    CSVParser->>CSVParser: extract_column_names(data)
    CSVParser->>CSVParser: extract_data_rows(data)
    CSVParser->>FileManager: close_file(file)
    CSVParser-->>CLI: data
    CLI->>JSONGenerator: convert_to_json(data, schema)
    JSONGenerator->>FileManager: open_file(json_filepath, 'w')
    FileManager-->>JSONGenerator: file
    JSONGenerator->>FileManager: write_json(file, json_data)
    JSONGenerator->>FileManager: close_file(file)
    JSONGenerator-->>CLI: Success
    CLI-->>User: JSON file created