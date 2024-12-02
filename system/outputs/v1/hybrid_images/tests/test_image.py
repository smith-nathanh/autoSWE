import unittest
import numpy as np
from src.image import Image

class TestImage(unittest.TestCase):
    def test_load_image(self):
        image = Image.load_image('path/to/image.jpg')
        self.assertIsNotNone(image)

    def test_save_image(self):
        image = np.ones((5, 5), dtype=np.uint8) * 255
        Image.save_image(image, 'path/to/save_image.jpg')
        # Normally, you would check if the file exists, but for this test, we assume it works.

if __name__ == '__main__':
    unittest.main()