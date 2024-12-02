classDiagram
    class QueryArXiv {
        - String category
        - String title
        - String author
        - String abstract
        - int recent_days
        - int max_results
        - boolean verbose
        - String to_file
        + void executeQuery()
        + void fetchResults()
        + void filterResultsByDate()
        + void outputResults()
    }

    class ArXivAPI {
        + String constructQueryURL(String category, String title, String author, String abstract, int max_results)
        + XML fetchData(String url)
    }

    class XMLParser {
        + List parseXML(XML data)
    }

    class CSVExporter {
        + void exportToCSV(List results, String filePath)
    }

    QueryArXiv --> ArXivAPI : uses
    QueryArXiv --> XMLParser : uses
    QueryArXiv --> CSVExporter : uses