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
        +fetch_data(): str
        +parse_xml_data(xml_data: str): List[Paper]
        +filter_by_date(papers: List[Paper]): List[Paper]
        +output_results(papers: List[Paper]): void
    }

    class Paper {
        -category: str
        -title: str
        -author: str
        -abstract: str
        -published: date
        -link: str
    }

    QueryArXiv --> Paper