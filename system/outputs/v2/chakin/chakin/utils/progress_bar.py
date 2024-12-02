from progressbar import ProgressBar as PB

class ProgressBar:
    def __init__(self):
        self.pb = PB(max_value=100)

    def start(self):
        for i in range(100):
            self.pb.update(i)

    def finish(self):
        self.pb.finish()