import cv2
import numpy as np

class ImageProcessor:
    @staticmethod
    def apply_convolution(image, kernel):
        return cv2.filter2D(image, -1, kernel)

    @staticmethod
    def apply_cross_correlation(image, kernel):
        return cv2.matchTemplate(image, kernel, cv2.TM_CCORR_NORMED)

    @staticmethod
    def apply_gaussian_blur(image, sigma, kernel_size):
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    @staticmethod
    def apply_low_pass_filter(image, sigma, kernel_size):
        return ImageProcessor.apply_gaussian_blur(image, sigma, kernel_size)

    @staticmethod
    def apply_high_pass_filter(image, sigma, kernel_size):
        low_pass = ImageProcessor.apply_low_pass_filter(image, sigma, kernel_size)
        return cv2.subtract(image, low_pass)