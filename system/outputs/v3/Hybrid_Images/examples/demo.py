import cv2
import numpy as np
from src.hybrid_image_creator import HybridImageCreator

# Load sample images
image1 = cv2.imread('examples/sample_images/image1.jpg', cv2.IMREAD_COLOR)
image2 = cv2.imread('examples/sample_images/image2.jpg', cv2.IMREAD_COLOR)

# Parameters for hybrid image creation
mix_ratio = 0.5
filter_type1 = 'low'
filter_type2 = 'high'

# Create HybridImageCreator instance
hybrid_creator = HybridImageCreator()

# Create hybrid image
hybrid_image = hybrid_creator.create_hybrid_image(image1, image2, mix_ratio, filter_type1, filter_type2)

# Display the hybrid image
cv2.imshow('Hybrid Image', hybrid_image)
cv2.waitKey(0)
cv2.destroyAllWindows()