classDiagram
    class Chakin {
        +search(lang: str): List[str]
        +download(number: int, save_dir: str): void
    }
    class Dataset {
        -name: str
        -dimension: int
        -corpus: str
        -vocabularySize: str
        -method: str
        -language: str
        -paper: str
        -author: str
        -url: str
    }
    class CSVHandler {
        +readCSV(filePath: str): List[Dataset]
    }
    Chakin --> CSVHandler : uses
    CSVHandler --> Dataset : creates