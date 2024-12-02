sequenceDiagram
    participant User
    participant CommandLineInterface
    participant QueryArXiv
    participant ArXivAPI
    participant CSVWriter

    User->>CommandLineInterface: Provide search parameters
    CommandLineInterface->>QueryArXiv: Initialize with parameters
    QueryArXiv->>QueryArXiv: construct_query_url()
    QueryArXiv->>ArXivAPI: fetch_data()
    ArXivAPI-->>QueryArXiv: Return XML data
    QueryArXiv->>QueryArXiv: parse_xml_data(xml_data)
    QueryArXiv->>QueryArXiv: filter_by_date(papers)
    alt verbose is true
        QueryArXiv->>CommandLineInterface: output_results(papers)
    end
    alt to_file is specified
        QueryArXiv->>CSVWriter: output_results(papers)
    end