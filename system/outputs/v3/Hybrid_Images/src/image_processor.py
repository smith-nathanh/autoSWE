import cv2
import numpy as np

class ImageProcessor:
    def apply_low_pass_filter(self, image, sigma, kernel_size):
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    def apply_high_pass_filter(self, image, sigma, kernel_size):
        low_pass = self.apply_low_pass_filter(image, sigma, kernel_size)
        return cv2.subtract(image, low_pass)

    def apply_gaussian_blur(self, image, sigma, kernel_size):
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    def cross_correlation(self, image1, image2):
        return cv2.matchTemplate(image1, image2, cv2.TM_CCORR_NORMED)

    def convolution(self, image1, image2):
        return cv2.filter2D(image1, -1, image2)