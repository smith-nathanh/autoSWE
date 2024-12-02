classDiagram
    class CSVParser {
        +read_csv(filepath: str, delimiter: str) List[Dict[str, Any]]
        +extract_column_names(data: List[Dict[str, Any]]) List[str]
        +extract_data_rows(data: List[Dict[str, Any]]) List[Dict[str, Any]]
    }
    class JSONGenerator {
        +convert_to_json(data: List[Dict[str, Any]], schema: Dict[str, Any]) str
        +output_json(data: str, filepath: str)
    }
    class CLI {
        +parse_arguments() Dict[str, Any]
        +execute_conversion(args: Dict[str, Any])
    }
    class FileManager {
        +open_file(filepath: str, mode: str)
        +close_file(file)
    }
    class ContextManager {
        +__enter__()
        +__exit__()
    }
    CSVParser --> JSONGenerator
    CLI --> CSVParser
    CLI --> JSONGenerator
    FileManager --> ContextManager
    JSONGenerator --> FileManager