classDiagram
    class Chakin {
        +search(lang: str): List[str]
        +download(number: int, save_dir: str): void
    }
    class Dataset {
        +Name: str
        +Dimension: int
        +Corpus: str
        +VocabularySize: str
        +Method: str
        +Language: str
        +Paper: str
        +Author: str
        +URL: str
    }
    class CSVHandler {
        +load_csv(file_path: str): List[Dataset]
        +search_by_language(language: str): List[Dataset]
    }
    class ProgressBar {
        +start(): void
        +update(progress: int): void
        +finish(): void
    }
    Chakin --> CSVHandler : uses
    Chakin --> ProgressBar : uses
    CSVHandler --> Dataset : manages