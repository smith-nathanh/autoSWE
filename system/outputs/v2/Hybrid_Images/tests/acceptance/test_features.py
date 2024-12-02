import unittest
import cv2
import numpy as np
from src.image import Image
from src.hybrid_image_creator import HybridImageCreator

class TestFeatures(unittest.TestCase):
    def setUp(self):
        # Create two simple test images
        self.image1 = np.ones((100, 100, 3), dtype=np.uint8) * 255  # White image
        self.image2 = np.zeros((100, 100, 3), dtype=np.uint8)       # Black image
        self.creator = HybridImageCreator()

    def test_hybrid_image_creation(self):
        # Test the creation of a hybrid image
        hybrid_image = self.creator.createHybridImage(self.image1, self.image2, 0.5, 'low', 'high')
        self.assertEqual(hybrid_image.shape, self.image1.shape)
        # Check if the hybrid image is a blend of the two images
        self.assertTrue(np.any(hybrid_image != self.image1))
        self.assertTrue(np.any(hybrid_image != self.image2))

    def test_image_processing_operations(self):
        # Test Gaussian Blur
        blurred_image = cv2.GaussianBlur(self.image1, (5, 5), 1)
        self.assertEqual(blurred_image.shape, self.image1.shape)

        # Test Low-Pass Filter
        low_pass_image = cv2.GaussianBlur(self.image1, (5, 5), 0)
        self.assertEqual(low_pass_image.shape, self.image1.shape)

        # Test High-Pass Filter
        low_pass = cv2.GaussianBlur(self.image1, (5, 5), 0)
        high_pass_image = cv2.subtract(self.image1, low_pass)
        self.assertEqual(high_pass_image.shape, self.image1.shape)

    def test_image_loading_and_saving(self):
        # Test loading and saving of images
        image = Image()
        image.loadImage('path/to/image1.jpg')
        self.assertIsNotNone(image.data)

        Image.saveImage(image.data, 'output_test_image.jpg')
        self.assertTrue(os.path.exists('output_test_image.jpg'))
        os.remove('output_test_image.jpg')

if __name__ == '__main__':
    unittest.main()
