import unittest
import cv2
import numpy as np
from src.image_processor import ImageProcessor
from src.hybrid_image_creator import HybridImageCreator

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image = np.ones((100, 100, 3), dtype=np.uint8) * 255  # white image

    def test_apply_low_pass_filter(self):
        blurred_image = self.processor.apply_low_pass_filter(self.image, sigma=5, kernel_size=15)
        self.assertEqual(blurred_image.shape, self.image.shape)

    def test_apply_high_pass_filter(self):
        high_pass_image = self.processor.apply_high_pass_filter(self.image, sigma=5, kernel_size=15)
        self.assertEqual(high_pass_image.shape, self.image.shape)

    def test_apply_gaussian_blur(self):
        blurred_image = self.processor.apply_gaussian_blur(self.image, sigma=5, kernel_size=15)
        self.assertEqual(blurred_image.shape, self.image.shape)

    def test_cross_correlation(self):
        result = self.processor.cross_correlation(self.image, self.image)
        self.assertIsNotNone(result)

    def test_convolution(self):
        kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
        convolved_image = self.processor.convolution(self.image, kernel)
        self.assertEqual(convolved_image.shape, self.image.shape)

class TestHybridImageCreator(unittest.TestCase):
    def setUp(self):
        self.creator = HybridImageCreator()
        self.image1 = np.ones((100, 100, 3), dtype=np.uint8) * 255  # white image
        self.image2 = np.zeros((100, 100, 3), dtype=np.uint8)  # black image

    def test_create_hybrid_image(self):
        hybrid_image = self.creator.create_hybrid_image(self.image1, self.image2, mix_ratio=0.5, filter_type1='low', filter_type2='high')
        self.assertEqual(hybrid_image.shape, self.image1.shape)

if __name__ == '__main__':
    unittest.main()
