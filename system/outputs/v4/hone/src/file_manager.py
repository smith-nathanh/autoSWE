class FileManager:
    def open_file(self, filepath, mode):
        return open(filepath, mode, encoding='utf-8')

    def close_file(self, file):
        file.close()
