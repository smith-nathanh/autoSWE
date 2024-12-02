import unittest
import cv2
import numpy as np
from src.hybrid_image_creator import HybridImageCreator

class TestHybridImageFeatures(unittest.TestCase):
    def setUp(self):
        # Load sample images
        self.image1 = cv2.imread('examples/sample_images/image1.jpg', cv2.IMREAD_COLOR)
        self.image2 = cv2.imread('examples/sample_images/image2.jpg', cv2.IMREAD_COLOR)
        self.hybrid_creator = HybridImageCreator()

    def test_low_pass_filter(self):
        # Test low-pass filter application
        low_pass_image = self.hybrid_creator.processor.apply_low_pass_filter(self.image1, sigma=5, kernel_size=15)
        self.assertIsNotNone(low_pass_image)
        self.assertEqual(low_pass_image.shape, self.image1.shape)

    def test_high_pass_filter(self):
        # Test high-pass filter application
        high_pass_image = self.hybrid_creator.processor.apply_high_pass_filter(self.image1, sigma=5, kernel_size=15)
        self.assertIsNotNone(high_pass_image)
        self.assertEqual(high_pass_image.shape, self.image1.shape)

    def test_create_hybrid_image(self):
        # Test hybrid image creation
        mix_ratio = 0.5
        filter_type1 = 'low'
        filter_type2 = 'high'
        hybrid_image = self.hybrid_creator.create_hybrid_image(self.image1, self.image2, mix_ratio, filter_type1, filter_type2)
        self.assertIsNotNone(hybrid_image)
        self.assertEqual(hybrid_image.shape, self.image1.shape)

    def test_hybrid_image_content(self):
        # Test that hybrid image contains features from both images
        mix_ratio = 0.5
        filter_type1 = 'low'
        filter_type2 = 'high'
        hybrid_image = self.hybrid_creator.create_hybrid_image(self.image1, self.image2, mix_ratio, filter_type1, filter_type2)
        # Check if hybrid image is a blend of both images
        diff1 = cv2.absdiff(hybrid_image, self.image1)
        diff2 = cv2.absdiff(hybrid_image, self.image2)
        self.assertTrue(np.any(diff1) and np.any(diff2))

if __name__ == '__main__':
    unittest.main()
