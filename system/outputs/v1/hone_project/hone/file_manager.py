# file_manager.py

class FileManager:
    def open_file(self, filepath: str, mode: str):
        return open(filepath, mode)

    def close_file(self, file):
        file.close()