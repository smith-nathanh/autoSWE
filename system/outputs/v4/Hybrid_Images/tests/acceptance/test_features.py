import unittest
import cv2
import numpy as np
from src.image import Image
from src.hybrid_image_creator import HybridImageCreator

class TestFeatures(unittest.TestCase):
    def setUp(self):
        # Load example images
        self.image1 = Image.load_image('examples/image1.jpg')
        self.image2 = Image.load_image('examples/image2.jpg')
        self.creator = HybridImageCreator()

    def test_hybrid_image_creation(self):
        # Test hybrid image creation with specified parameters
        hybrid_image = self.creator.create_hybrid_image(self.image1, self.image2, 0.5, 'low', 'high', 5, 15)
        self.assertIsNotNone(hybrid_image, "Hybrid image should not be None")
        
        # Check if the hybrid image has the same dimensions as the input images
        self.assertEqual(hybrid_image.shape, self.image1.shape, "Hybrid image should have the same dimensions as input images")

    def test_image_processing_operations(self):
        # Test Gaussian blur
        processor = self.creator.processor
        blurred_image = processor.apply_gaussian_blur(self.image1, 1, 3)
        self.assertIsNotNone(blurred_image, "Blurred image should not be None")

        # Test low-pass filter
        low_pass_image = processor.apply_low_pass_filter(self.image1, 1, 3)
        self.assertIsNotNone(low_pass_image, "Low-pass filtered image should not be None")

        # Test high-pass filter
        high_pass_image = processor.apply_high_pass_filter(self.image1, 1, 3)
        self.assertIsNotNone(high_pass_image, "High-pass filtered image should not be None")

if __name__ == '__main__':
    unittest.main()
