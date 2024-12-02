class LanguageDetector:
    def detect_language(self, file_extension):
        if file_extension == '.py':
            return 'python'
        elif file_extension == '.js':
            return 'javascript'
        else:
            return 'unknown'