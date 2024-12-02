import unittest
import cv2
import numpy as np
from src.image import Image
from src.hybrid_image_creator import HybridImageCreator

class TestFeatures(unittest.TestCase):
    def setUp(self):
        # Create two simple test images
        self.image1 = np.ones((100, 100, 3), dtype=np.uint8) * 255  # White image
        self.image2 = np.zeros((100, 100, 3), dtype=np.uint8)  # Black image
        self.creator = HybridImageCreator()

    def test_hybrid_image_creation(self):
        # Test the creation of a hybrid image
        hybrid_image = self.creator.create_hybrid_image(self.image1, self.image2, mix_ratio=0.5, filter_type1='low', filter_type2='high')
        self.assertIsNotNone(hybrid_image)
        self.assertEqual(hybrid_image.shape, self.image1.shape)

    def test_image_processing_operations(self):
        # Test low-pass filter
        low_pass_image = cv2.GaussianBlur(self.image1, (15, 15), 5)
        self.assertIsNotNone(low_pass_image)

        # Test high-pass filter
        low_pass = cv2.GaussianBlur(self.image1, (15, 15), 5)
        high_pass_image = cv2.subtract(self.image1, low_pass)
        self.assertIsNotNone(high_pass_image)

    def test_image_load_and_save(self):
        # Test loading and saving an image
        Image.save_image(self.image1, 'test_image.jpg')
        loaded_image = Image.load_image('test_image.jpg')
        self.assertIsNotNone(loaded_image)
        self.assertEqual(loaded_image.shape, self.image1.shape)

if __name__ == '__main__':
    unittest.main()
