classDiagram
    class Chakin {
        +search(lang: str): List[WordVector]
        +download(number: int, save_dir: str): void
    }
    class WordVector {
        +name: str
        +dimension: int
        +corpus: str
        +vocabularySize: int
        +method: str
        +language: str
        +paper: str
        +author: str
        +url: str
    }
    class DatasetManager {
        +loadDatasets(filePath: str): List[WordVector]
        +getVectorsByLanguage(language: str): List[WordVector]
    }
    class ProgressBar {
        +start()
        +update(progress: float)
        +finish()
    }
    Chakin --> DatasetManager
    Chakin --> ProgressBar
    DatasetManager --> WordVector