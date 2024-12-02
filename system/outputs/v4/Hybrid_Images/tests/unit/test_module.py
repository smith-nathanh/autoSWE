import unittest
import numpy as np
import cv2
from src.image_processor import ImageProcessor
from src.hybrid_image_creator import HybridImageCreator
from src.image import Image

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image = np.ones((100, 100), dtype=np.uint8) * 255
        self.kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

    def test_apply_convolution(self):
        result = self.processor.apply_convolution(self.image, self.kernel)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_cross_correlation(self):
        result = self.processor.apply_cross_correlation(self.image, self.kernel)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_gaussian_blur(self):
        result = self.processor.apply_gaussian_blur(self.image, 1, 3)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_low_pass_filter(self):
        result = self.processor.apply_low_pass_filter(self.image, 1, 3)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, self.image.shape)

    def test_apply_high_pass_filter(self):
        result = self.processor.apply_high_pass_filter(self.image, 1, 3)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, self.image.shape)

    def test_invalid_kernel_size(self):
        with self.assertRaises(cv2.error):
            self.processor.apply_gaussian_blur(self.image, 1, -1)

class TestHybridImageCreator(unittest.TestCase):
    def setUp(self):
        self.creator = HybridImageCreator()
        self.image1 = np.ones((100, 100), dtype=np.uint8) * 255
        self.image2 = np.zeros((100, 100), dtype=np.uint8)

    def test_create_hybrid_image(self):
        hybrid_image = self.creator.create_hybrid_image(self.image1, self.image2, 0.5, 'low', 'high', 5, 15)
        self.assertIsNotNone(hybrid_image)
        self.assertEqual(hybrid_image.shape, self.image1.shape)

    def test_invalid_mix_ratio(self):
        with self.assertRaises(ValueError):
            self.creator.create_hybrid_image(self.image1, self.image2, 1.5, 'low', 'high', 5, 15)

    def test_invalid_filter_type(self):
        with self.assertRaises(ValueError):
            self.creator.create_hybrid_image(self.image1, self.image2, 0.5, 'invalid', 'high', 5, 15)

class TestImage(unittest.TestCase):
    def test_load_image(self):
        image = Image.load_image('examples/image1.jpg')
        self.assertIsNotNone(image)

    def test_save_image(self):
        image = np.ones((100, 100), dtype=np.uint8) * 255
        Image.save_image(image, 'examples/test_image.jpg')
        loaded_image = Image.load_image('examples/test_image.jpg')
        self.assertTrue(np.array_equal(image, loaded_image))

if __name__ == '__main__':
    unittest.main()
