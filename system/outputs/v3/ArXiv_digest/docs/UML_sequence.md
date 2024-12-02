sequenceDiagram
    participant User
    participant QueryArXiv
    participant ArXivAPI
    participant XMLParser
    participant CSVExporter

    User->>QueryArXiv: Run query with parameters
    QueryArXiv->>QueryArXiv: construct_query_url()
    QueryArXiv->>ArXivAPI: fetch_data(query_url)
    ArXivAPI-->>QueryArXiv: XML data
    QueryArXiv->>XMLParser: parse(XML data)
    XMLParser-->>QueryArXiv: List of results
    QueryArXiv->>QueryArXiv: check_date(results)
    alt to_file specified
        QueryArXiv->>CSVExporter: export_to_csv(results, file_path)
    end
    alt verbose specified
        QueryArXiv->>User: output_results(results)
    end