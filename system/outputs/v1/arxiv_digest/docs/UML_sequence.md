sequenceDiagram
    participant User
    participant CommandLineInterface
    participant QueryArXiv
    participant ArXivAPI
    participant XMLParser
    participant CSVExporter

    User ->> CommandLineInterface: Run query_arxiv.py with parameters
    CommandLineInterface ->> QueryArXiv: Initialize with parameters
    QueryArXiv ->> ArXivAPI: Construct query URL
    ArXivAPI ->> QueryArXiv: Return query URL
    QueryArXiv ->> ArXivAPI: Fetch data from ArXiv
    ArXivAPI ->> QueryArXiv: Return XML data
    QueryArXiv ->> XMLParser: Parse XML data
    XMLParser ->> QueryArXiv: Return parsed results
    QueryArXiv ->> QueryArXiv: Filter results by date
    alt Output to console
        QueryArXiv ->> User: Display results
    end
    alt Output to CSV
        QueryArXiv ->> CSVExporter: Export results to CSV
        CSVExporter ->> QueryArXiv: Confirm export
    end