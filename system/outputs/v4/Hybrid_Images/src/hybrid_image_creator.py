from .image_processor import ImageProcessor
from .image import Image

class HybridImageCreator:
    def __init__(self):
        self.processor = ImageProcessor()

    def create_hybrid_image(self, image1, image2, mix_ratio, filter_type1, filter_type2, sigma, kernel_size):
        """Create a hybrid image from two images using specified filters and mix ratio."""
        if filter_type1 == 'low':
            image1_filtered = self.processor.apply_low_pass_filter(image1, sigma, kernel_size)
        else:
            image1_filtered = self.processor.apply_high_pass_filter(image1, sigma, kernel_size)

        if filter_type2 == 'low':
            image2_filtered = self.processor.apply_low_pass_filter(image2, sigma, kernel_size)
        else:
            image2_filtered = self.processor.apply_high_pass_filter(image2, sigma, kernel_size)

        hybrid_image = cv2.addWeighted(image1_filtered, mix_ratio, image2_filtered, 1 - mix_ratio, 0)
        return hybrid_image
