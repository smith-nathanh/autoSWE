import contextlib

class Utilities:
    @staticmethod
    @contextlib.contextmanager
    def open_file(filepath, mode):
        file = open(filepath, mode)
        try:
            yield file
        finally:
            file.close()

    @staticmethod
    def manage_file(file):
        # Placeholder for any additional file management logic
        pass
