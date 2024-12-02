# chakin/progress_bar.py

class ProgressBar:
    def __init__(self, total):
        self.total = total
        self.current = 0

    def start(self):
        print("Download started...")

    def update(self, progress):
        self.current += progress
        percent = (self.current / self.total) * 100
        print(f"Progress: {percent:.2f}%", end='\r')

    def finish(self):
        print("Download complete!")
