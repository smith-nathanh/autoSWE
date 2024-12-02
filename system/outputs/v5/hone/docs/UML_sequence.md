sequenceDiagram
    participant User
    participant CLI
    participant CSVParser
    participant JSONGenerator
    participant FileManager
    User->>CLI: Run conversion command
    CLI->>CSVParser: parse_arguments(args)
    CSVParser->>FileManager: open_file(csv_filepath, 'r')
    FileManager-->>CSVParser: file
    CSVParser->>CSVParser: read_csv(file, delimiter)
    CSVParser->>CSVParser: extract_column_names()
    CSVParser->>CSVParser: extract_data_rows()
    CSVParser->>FileManager: close_file(file)
    CLI->>JSONGenerator: convert_to_json(data, schema)
    JSONGenerator->>FileManager: open_file(json_filepath, 'w')
    FileManager-->>JSONGenerator: file
    JSONGenerator->>JSONGenerator: output_json(data, file)
    JSONGenerator->>FileManager: close_file(file)
    CLI-->>User: JSON file created