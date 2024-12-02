import numpy as np
import cv2

class ImageProcessor:
    def apply_convolution(self, image, kernel):
        """Apply convolution to an image using a specified kernel."""
        return cv2.filter2D(image, -1, kernel)

    def apply_cross_correlation(self, image, kernel):
        """Apply cross-correlation to an image using a specified kernel."""
        kernel = np.flipud(np.fliplr(kernel))  # Flip the kernel for cross-correlation
        return cv2.filter2D(image, -1, kernel)

    def apply_gaussian_blur(self, image, sigma, kernel_size):
        """Apply Gaussian blur to an image using a specified sigma and kernel size."""
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    def apply_low_pass_filter(self, image, sigma, kernel_size):
        """Apply a low-pass filter to an image using Gaussian blur."""
        return self.apply_gaussian_blur(image, sigma, kernel_size)

    def apply_high_pass_filter(self, image, sigma, kernel_size):
        """Apply a high-pass filter to an image by subtracting the low-pass filtered image from the original."""
        low_pass = self.apply_low_pass_filter(image, sigma, kernel_size)
        return cv2.subtract(image, low_pass)
