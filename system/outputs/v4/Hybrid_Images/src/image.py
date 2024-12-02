import cv2

class Image:
    @staticmethod
    def load_image(file_path):
        """Load an image from a file path."""
        return cv2.imread(file_path)

    @staticmethod
    def save_image(image, file_path):
        """Save an image to a file path."""
        cv2.imwrite(file_path, image)
