import cv2

class Image:
    def __init__(self):
        self.data = None

    def loadImage(self, filePath):
        self.data = cv2.imread(filePath)

    @staticmethod
    def saveImage(image, filePath):
        cv2.imwrite(filePath, image)