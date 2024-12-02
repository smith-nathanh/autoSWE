class LanguageDetector:
    LANGUAGE_MAP = {
        'py': 'Python',
        'js': 'JavaScript',
        'java': 'Java',
        'cpp': 'C++',
        'c': 'C',
        'rb': 'Ruby',
        'go': 'Go',
        'rs': 'Rust',
        'php': 'PHP',
        'swift': 'Swift',
    }

    def detectLanguage(self, filename):
        extension = filename.split('.')[-1]
        return self.LANGUAGE_MAP.get(extension, 'Unknown')