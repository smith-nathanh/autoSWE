import os

class FileManager:
    def createFile(self, file_name, content):
        with open(file_name, 'w') as file:
            file.write(content)

    def detectLanguage(self, file_extension):
        # Simple mapping of file extensions to languages
        language_map = {
            'py': 'Python',
            'js': 'JavaScript',
            'java': 'Java',
            'cpp': 'C++',
            'c': 'C',
            'rb': 'Ruby',
            'go': 'Go',
            'rs': 'Rust',
        }
        return language_map.get(file_extension, 'Unknown')

    def formatHeader(self, content, language):
        # Simple header formatting based on language
        if language == 'Python':
            return f"""""\n{content}\n"""""
        elif language == 'JavaScript':
            return f"/*\n{content}\n*/"
        elif language == 'Java':
            return f"/*\n{content}\n*/"
        elif language == 'C++':
            return f"/*\n{content}\n*/"
        elif language == 'C':
            return f"/*\n{content}\n*/"
        elif language == 'Ruby':
            return f"=begin\n{content}\n=end"
        elif language == 'Go':
            return f"/*\n{content}\n*/"
        elif language == 'Rust':
            return f"/*\n{content}\n*/"
        else:
            return content