import cv2
from src.hybrid_image_creator import HybridImageCreator

# Load images
image1 = cv2.imread('path_to_image1.jpg', cv2.IMREAD_COLOR)
image2 = cv2.imread('path_to_image2.jpg', cv2.IMREAD_COLOR)

# Parameters
mix_ratio = 0.5
filter_type1 = 'low'
filter_type2 = 'high'
sigma = 5
kernel_size = 15

# Create hybrid image
creator = HybridImageCreator()
hybrid_image = creator.create_hybrid_image(image1, image2, mix_ratio, filter_type1, filter_type2, sigma, kernel_size)

# Display the result
cv2.imshow('Hybrid Image', hybrid_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
