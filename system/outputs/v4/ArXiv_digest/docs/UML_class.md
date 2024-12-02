classDiagram
    class QueryArXiv {
        - String category
        - String title
        - String author
        - String abstract
        - int recent_days
        - int max_results
        - String to_file
        - boolean verbose
        + executeQuery()
        + constructQueryURL()
        + checkDate()
        + outputResults()
    }
    class APIInteraction {
        + fetchData(String url)
    }
    class XMLParser {
        + parseData(String xmlData)
    }
    class CommandLineInterface {
        + parseArguments(String[] args)
    }
    class OutputHandler {
        + printToConsole(String data)
        + saveToCSV(String data, String filePath)
    }
    QueryArXiv --> APIInteraction : uses
    QueryArXiv --> XMLParser : uses
    QueryArXiv --> CommandLineInterface : uses
    QueryArXiv --> OutputHandler : uses