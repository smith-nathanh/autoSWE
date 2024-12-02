import unittest
import numpy as np
import cv2
from src.image_processor import ImageProcessor
from src.hybrid_image_creator import HybridImageCreator

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

    def test_apply_gaussian_blur_invalid_sigma(self):
        with self.assertRaises(cv2.error):
            self.processor.apply_gaussian_blur(self.image, sigma=-1, kernel_size=3)

    def test_apply_low_pass_filter(self):
        result = self.processor.apply_low_pass_filter(self.image, sigma=1, kernel_size=3)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_high_pass_filter(self):
        result = self.processor.apply_high_pass_filter(self.image, sigma=1, kernel_size=3)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_high_pass_filter_invalid_image(self):
        with self.assertRaises(cv2.error):
            self.processor.apply_high_pass_filter(np.array([]), sigma=1, kernel_size=3)

class TestHybridImageCreator(unittest.TestCase):
    def setUp(self):
        self.creator = HybridImageCreator()
        self.image1 = np.random.rand(100, 100, 3).astype(np.float32)
        self.image2 = np.random.rand(100, 100, 3).astype(np.float32)

    def test_create_hybrid_image(self):
        hybrid_image = self.creator.create_hybrid_image(
            self.image1, self.image2, mix_ratio=0.5, filter_type1='low', filter_type2='high', sigma=1, kernel_size=3
        )
        self.assertEqual(hybrid_image.shape, self.image1.shape)

    def test_create_hybrid_image_invalid_mix_ratio(self):
        with self.assertRaises(ValueError):
            self.creator.create_hybrid_image(
                self.image1, self.image2, mix_ratio=1.5, filter_type1='low', filter_type2='high', sigma=1, kernel_size=3
            )

    def test_create_hybrid_image_invalid_filter_type(self):
        with self.assertRaises(ValueError):
            self.creator.create_hybrid_image(
                self.image1, self.image2, mix_ratio=0.5, filter_type1='invalid', filter_type2='high', sigma=1, kernel_size=3
            )

    def test_create_hybrid_image_empty_images(self):
        with self.assertRaises(cv2.error):
            self.creator.create_hybrid_image(
                np.array([]), np.array([]), mix_ratio=0.5, filter_type1='low', filter_type2='high', sigma=1, kernel_size=3
            )

if __name__ == '__main__':
    unittest.main()
