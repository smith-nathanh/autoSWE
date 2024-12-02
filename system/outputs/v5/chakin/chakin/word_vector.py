class WordVector:
    def __init__(self, Name, Dimension, Corpus, VocabularySize, Method, Language, Paper, Author, URL):
        self.name = Name
        self.dimension = Dimension
        self.corpus = Corpus
        self.vocabularySize = VocabularySize
        self.method = Method
        self.language = Language
        self.paper = Paper
        self.author = Author
        self.url = URL

    def __repr__(self):
        return f"WordVector(name={self.name}, language={self.language})"
