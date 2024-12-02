import unittest
import numpy as np
from src.hybrid_image_creator import HybridImageCreator

class TestHybridImageCreator(unittest.TestCase):
    def setUp(self):
        self.image1 = np.ones((100, 100, 3), dtype=np.uint8) * 255
        self.image2 = np.zeros((100, 100, 3), dtype=np.uint8)
        self.creator = HybridImageCreator()

    def test_createHybridImage(self):
        hybrid_image = self.creator.createHybridImage(self.image1, self.image2, 0.5, 'low', 'high')
        self.assertEqual(hybrid_image.shape, self.image1.shape)

if __name__ == '__main__':
    unittest.main()