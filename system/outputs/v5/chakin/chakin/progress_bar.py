class ProgressBar:
    def start(self):
        print("Download started...")

    def update(self, progress):
        print(f"Progress: {progress}%")

    def finish(self):
        print("Download finished!")
