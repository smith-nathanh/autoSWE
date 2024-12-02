import unittest
import numpy as np
import cv2
from src.hybrid_image_creator import HybridImageCreator

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

if __name__ == '__main__':
    unittest.main()
