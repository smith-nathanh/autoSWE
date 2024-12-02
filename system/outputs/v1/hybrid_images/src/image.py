import cv2

class Image:
    @staticmethod
    def load_image(file_path):
        return cv2.imread(file_path)

    @staticmethod
    def save_image(image, file_path):
        cv2.imwrite(file_path, image)