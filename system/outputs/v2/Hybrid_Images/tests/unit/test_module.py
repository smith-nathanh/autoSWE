import unittest
import numpy as np
import cv2
from src.image_processor import ImageProcessor
from src.hybrid_image_creator import HybridImageCreator
from src.image import Image
import os

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.image = np.ones((100, 100, 3), dtype=np.uint8) * 255

    def test_applyGaussianBlur(self):
        blurred = ImageProcessor.applyGaussianBlur(self.image, 1, 5)
        self.assertEqual(blurred.shape, self.image.shape)

    def test_applyLowPassFilter(self):
        low_pass = ImageProcessor.applyLowPassFilter(self.image)
        self.assertEqual(low_pass.shape, self.image.shape)

    def test_applyHighPassFilter(self):
        high_pass = ImageProcessor.applyHighPassFilter(self.image)
        self.assertEqual(high_pass.shape, self.image.shape)

    def test_crossCorrelate(self):
        result = ImageProcessor.crossCorrelate(self.image, self.image)
        self.assertIsNotNone(result)

    def test_convolve(self):
        result = ImageProcessor.convolve(self.image, self.image)
        self.assertEqual(result.shape, self.image.shape)

class TestHybridImageCreator(unittest.TestCase):
    def setUp(self):
        self.image1 = np.ones((100, 100, 3), dtype=np.uint8) * 255
        self.image2 = np.zeros((100, 100, 3), dtype=np.uint8)
        self.creator = HybridImageCreator()

    def test_createHybridImage(self):
        hybrid_image = self.creator.createHybridImage(self.image1, self.image2, 0.5, 'low', 'high')
        self.assertEqual(hybrid_image.shape, self.image1.shape)

class TestImage(unittest.TestCase):
    def setUp(self):
        self.image = Image()
        self.test_image_path = 'test_image.jpg'
        # Create a dummy image for testing
        cv2.imwrite(self.test_image_path, np.ones((100, 100, 3), dtype=np.uint8) * 255)

    def tearDown(self):
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

    def test_loadImage(self):
        self.image.loadImage(self.test_image_path)
        self.assertIsNotNone(self.image.data)

    def test_saveImage(self):
        Image.saveImage(self.image.data, 'output_test_image.jpg')
        self.assertTrue(os.path.exists('output_test_image.jpg'))
        os.remove('output_test_image.jpg')

if __name__ == '__main__':
    unittest.main()
