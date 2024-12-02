import numpy as np

# Utility functions for creating filters can be added here if needed

# Example: Create a Gaussian kernel

def create_gaussian_kernel(kernel_size, sigma):
    """
    Create a Gaussian kernel given a kernel size and sigma.
    """
    ax = np.arange(-kernel_size // 2 + 1., kernel_size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    return kernel / np.sum(kernel)
