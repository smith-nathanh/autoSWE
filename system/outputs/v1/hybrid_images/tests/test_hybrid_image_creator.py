import unittest
import numpy as np
from src.hybrid_image_creator import HybridImageCreator

class TestHybridImageCreator(unittest.TestCase):
    def setUp(self):
        self.image1 = np.ones((5, 5), dtype=np.uint8) * 255
        self.image2 = np.zeros((5, 5), dtype=np.uint8)
        self.creator = HybridImageCreator()

    def test_create_hybrid_image(self):
        hybrid_image = self.creator.create_hybrid_image(self.image1, self.image2, mix_ratio=0.5, filter_type1='low', filter_type2='high')
        self.assertIsNotNone(hybrid_image)

if __name__ == '__main__':
    unittest.main()