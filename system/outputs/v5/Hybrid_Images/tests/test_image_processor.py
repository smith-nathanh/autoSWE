import unittest
import numpy as np
import cv2
from src.image_processor import ImageProcessor

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image = np.random.rand(100, 100, 3).astype(np.float32)
        self.kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)

    def test_apply_convolution(self):
        result = self.processor.apply_convolution(self.image, self.kernel)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_cross_correlation(self):
        result = self.processor.apply_cross_correlation(self.image, self.kernel)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_gaussian_blur(self):
        result = self.processor.apply_gaussian_blur(self.image, sigma=1, kernel_size=3)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_low_pass_filter(self):
        result = self.processor.apply_low_pass_filter(self.image, sigma=1, kernel_size=3)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_high_pass_filter(self):
        result = self.processor.apply_high_pass_filter(self.image, sigma=1, kernel_size=3)
        self.assertEqual(result.shape, self.image.shape)

if __name__ == '__main__':
    unittest.main()
