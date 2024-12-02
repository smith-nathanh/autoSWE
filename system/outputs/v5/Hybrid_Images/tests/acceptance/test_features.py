import unittest
import cv2
import numpy as np
from src.hybrid_image_creator import HybridImageCreator

class TestFeaturesAcceptance(unittest.TestCase):
    def setUp(self):
        self.creator = HybridImageCreator()
        # Create two simple test images
        self.image1 = np.ones((100, 100, 3), dtype=np.float32) * 255  # White image
        self.image2 = np.zeros((100, 100, 3), dtype=np.float32)  # Black image

    def test_hybrid_image_creation(self):
        """
        Acceptance test to ensure the hybrid image is created correctly
        and combines features from both images.
        """
        mix_ratio = 0.5
        filter_type1 = 'low'
        filter_type2 = 'high'
        sigma = 5
        kernel_size = 15

        hybrid_image = self.creator.create_hybrid_image(
            self.image1, self.image2, mix_ratio, filter_type1, filter_type2, sigma, kernel_size
        )

        # Check if the hybrid image has the same shape as the input images
        self.assertEqual(hybrid_image.shape, self.image1.shape)

        # Check if the hybrid image is not entirely black or white
        self.assertFalse(np.all(hybrid_image == 0) or np.all(hybrid_image == 255))

    def test_hybrid_image_with_different_filters(self):
        """
        Acceptance test to ensure the hybrid image creation works with different filter types.
        """
        mix_ratio = 0.7
        filter_type1 = 'high'
        filter_type2 = 'low'
        sigma = 3
        kernel_size = 9

        hybrid_image = self.creator.create_hybrid_image(
            self.image1, self.image2, mix_ratio, filter_type1, filter_type2, sigma, kernel_size
        )

        # Check if the hybrid image has the same shape as the input images
        self.assertEqual(hybrid_image.shape, self.image1.shape)

        # Check if the hybrid image is not entirely black or white
        self.assertFalse(np.all(hybrid_image == 0) or np.all(hybrid_image == 255))

if __name__ == '__main__':
    unittest.main()
