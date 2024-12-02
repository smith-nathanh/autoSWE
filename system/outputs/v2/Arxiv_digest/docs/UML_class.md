classDiagram
    class QueryArXiv {
        -category: str
        -title: str
        -author: str
        -abstract: str
        -recent_days: int
        -to_file: str
        -verbose: bool
        +execute_query(): void
        +construct_query_url(): str
        +check_date(published_date: str): bool
        +output_results(results: List[Dict]): void
    }

    class ArXivAPI {
        +fetch_data(query_url: str): str
    }

    class XMLParser {
        +parse(xml_data: str): List[Dict]
    }

    class CSVExporter {
        +export_to_csv(data: List[Dict], file_path: str): void
    }

    QueryArXiv --> ArXivAPI : uses
    QueryArXiv --> XMLParser : uses
    QueryArXiv --> CSVExporter : uses