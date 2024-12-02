import contextlib

class Utilities:
    @contextlib.contextmanager
    def open_file(self, filepath, mode):
        file = open(filepath, mode)
        try:
            yield file
        finally:
            file.close()