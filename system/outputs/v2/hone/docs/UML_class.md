classDiagram
    class CSVParser {
        +read_csv(filepath: str, delimiter: str) void
        +extract_column_names() list
        +extract_data_rows() list
    }
    class JSONGenerator {
        +convert_to_json(data: list, schema: dict) dict
        +output_json(data: dict, filepath: str) void
    }
    class Utilities {
        +open_file(filepath: str, mode: str) file
        +manage_file(file: file) void
    }
    class CLI {
        +parse_arguments(args: list) dict
        +execute_conversion(args: dict) void
    }
    CSVParser --> JSONGenerator : uses
    JSONGenerator --> Utilities : uses
    CLI --> CSVParser : interacts
    CLI --> JSONGenerator : interacts
    CLI --> Utilities : uses