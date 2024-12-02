import cv2
import numpy as np

class ImageProcessor:
    @staticmethod
    def applyGaussianBlur(image, sigma, kernelSize):
        return cv2.GaussianBlur(image, (kernelSize, kernelSize), sigma)

    @staticmethod
    def applyLowPassFilter(image):
        return cv2.GaussianBlur(image, (5, 5), 0)

    @staticmethod
    def applyHighPassFilter(image):
        low_pass = cv2.GaussianBlur(image, (5, 5), 0)
        return cv2.subtract(image, low_pass)

    @staticmethod
    def crossCorrelate(image1, image2):
        return cv2.matchTemplate(image1, image2, cv2.TM_CCORR_NORMED)

    @staticmethod
    def convolve(image1, image2):
        return cv2.filter2D(image1, -1, image2)