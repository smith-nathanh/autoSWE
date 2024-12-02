from progressbar import ProgressBar as PB

class ProgressBar:
    def __init__(self, total_size):
        self.progress = PB(max_value=total_size)

    def update(self, size):
        self.progress.update(size)

    def finish(self):
        self.progress.finish()
