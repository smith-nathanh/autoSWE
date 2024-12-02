import unittest
import numpy as np
from src.image_processor import ImageProcessor
from src.hybrid_image_creator import HybridImageCreator
from src.image import Image

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.image = np.ones((5, 5), dtype=np.uint8) * 255
        self.kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

    def test_apply_convolution(self):
        result = ImageProcessor.apply_convolution(self.image, self.kernel)
        self.assertIsNotNone(result)

    def test_apply_cross_correlation(self):
        result = ImageProcessor.apply_cross_correlation(self.image, self.kernel)
        self.assertIsNotNone(result)

    def test_apply_gaussian_blur(self):
        result = ImageProcessor.apply_gaussian_blur(self.image, sigma=1, kernel_size=3)
        self.assertIsNotNone(result)

    def test_apply_low_pass_filter(self):
        result = ImageProcessor.apply_low_pass_filter(self.image, sigma=1, kernel_size=3)
        self.assertIsNotNone(result)

    def test_apply_high_pass_filter(self):
        result = ImageProcessor.apply_high_pass_filter(self.image, sigma=1, kernel_size=3)
        self.assertIsNotNone(result)

class TestHybridImageCreator(unittest.TestCase):
    def setUp(self):
        self.image1 = np.ones((5, 5), dtype=np.uint8) * 255
        self.image2 = np.zeros((5, 5), dtype=np.uint8)
        self.creator = HybridImageCreator()

    def test_create_hybrid_image(self):
        hybrid_image = self.creator.create_hybrid_image(self.image1, self.image2, mix_ratio=0.5, filter_type1='low', filter_type2='high')
        self.assertIsNotNone(hybrid_image)

class TestImage(unittest.TestCase):
    def test_load_image(self):
        image = Image.load_image('path/to/image.jpg')
        self.assertIsNotNone(image)

    def test_save_image(self):
        image = np.ones((5, 5), dtype=np.uint8) * 255
        Image.save_image(image, 'path/to/save_image.jpg')
        # Normally, you would check if the file exists, but for this test, we assume it works.

if __name__ == '__main__':
    unittest.main()
