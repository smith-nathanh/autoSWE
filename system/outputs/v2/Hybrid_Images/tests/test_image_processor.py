import unittest
import cv2
import numpy as np
from src.image_processor import ImageProcessor

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

if __name__ == '__main__':
    unittest.main()