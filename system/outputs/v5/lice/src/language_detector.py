class LanguageDetector:
    def detectLanguage(self, filename):
        extension = filename.split('.')[-1]
        language_map = {
            'py': 'Python',
            'js': 'JavaScript',
            'java': 'Java',
            'cpp': 'C++',
            'c': 'C',
            'rb': 'Ruby',
            'go': 'Go',
            'rs': 'Rust',
            'php': 'PHP',
            'html': 'HTML',
            'css': 'CSS',
        }
        return language_map.get(extension, 'Unknown')