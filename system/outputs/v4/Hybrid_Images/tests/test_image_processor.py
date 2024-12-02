import unittest
import numpy as np
import cv2
from src.image_processor import ImageProcessor

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image = np.ones((100, 100), dtype=np.uint8) * 255
        self.kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

    def test_apply_convolution(self):
        result = self.processor.apply_convolution(self.image, self.kernel)
        self.assertIsNotNone(result)

    def test_apply_cross_correlation(self):
        result = self.processor.apply_cross_correlation(self.image, self.kernel)
        self.assertIsNotNone(result)

    def test_apply_gaussian_blur(self):
        result = self.processor.apply_gaussian_blur(self.image, 1, 3)
        self.assertIsNotNone(result)

    def test_apply_low_pass_filter(self):
        result = self.processor.apply_low_pass_filter(self.image, 1, 3)
        self.assertIsNotNone(result)

    def test_apply_high_pass_filter(self):
        result = self.processor.apply_high_pass_filter(self.image, 1, 3)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
