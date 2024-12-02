sequenceDiagram
    participant User
    participant CommandLineInterface
    participant QueryArXiv
    participant APIInteraction
    participant XMLParser
    participant OutputHandler
    User->>CommandLineInterface: Provide search parameters
    CommandLineInterface->>QueryArXiv: Parse and validate arguments
    QueryArXiv->>APIInteraction: Construct query URL and fetch data
    APIInteraction->>QueryArXiv: Return raw XML data
    QueryArXiv->>XMLParser: Parse XML data
    XMLParser->>QueryArXiv: Return parsed data
    QueryArXiv->>QueryArXiv: Filter data by recent_days
    QueryArXiv->>OutputHandler: Output results
    OutputHandler->>User: Display results or save to CSV