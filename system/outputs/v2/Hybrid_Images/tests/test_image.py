import unittest
import os
import cv2
from src.image import Image

class TestImage(unittest.TestCase):
    def setUp(self):
        self.image = Image()
        self.test_image_path = 'test_image.jpg'
        self.image.data = cv2.imread(self.test_image_path)

    def test_loadImage(self):
        self.image.loadImage(self.test_image_path)
        self.assertIsNotNone(self.image.data)

    def test_saveImage(self):
        Image.saveImage(self.image.data, 'output_test_image.jpg')
        self.assertTrue(os.path.exists('output_test_image.jpg'))
        os.remove('output_test_image.jpg')

if __name__ == '__main__':
    unittest.main()