classDiagram
    class Chakin {
        +search(lang: String): List
        +download(number: int, save_dir: String): void
    }
    class Dataset {
        -name: String
        -dimension: int
        -corpus: String
        -vocabularySize: String
        -method: String
        -language: String
        -paper: String
        -author: String
        -url: String
    }
    class CSVHandler {
        +loadCSV(filePath: String): List
        +parseCSV(): List<Dataset>
    }
    Chakin --> CSVHandler : uses
    CSVHandler --> Dataset : creates