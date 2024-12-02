import unittest
import numpy as np
from src.image import Image
from src.hybrid_image_creator import HybridImageCreator

class TestHybridImageCreator(unittest.TestCase):
    def setUp(self):
        self.creator = HybridImageCreator()
        self.image1 = np.ones((100, 100), dtype=np.uint8) * 255
        self.image2 = np.zeros((100, 100), dtype=np.uint8)

    def test_create_hybrid_image(self):
        hybrid_image = self.creator.create_hybrid_image(self.image1, self.image2, 0.5, 'low', 'high', 5, 15)
        self.assertIsNotNone(hybrid_image)

if __name__ == '__main__':
    unittest.main()
