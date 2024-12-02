import unittest
import numpy as np
from src.image_processor import ImageProcessor

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

if __name__ == '__main__':
    unittest.main()