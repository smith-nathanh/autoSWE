import cv2
import numpy as np
from src.hybrid_image_creator import HybridImageCreator
from src.image import Image

# Load images
image1 = Image()
image1.loadImage('path/to/image1.jpg')

image2 = Image()
image2.loadImage('path/to/image2.jpg')

# Create hybrid image
creator = HybridImageCreator()
hybrid_image = creator.createHybridImage(image1.data, image2.data, mixRatio=0.5, filterType1='low', filterType2='high')

# Save hybrid image
hybrid_image_path = 'path/to/hybrid_image.jpg'
Image.saveImage(hybrid_image, hybrid_image_path)

# Display hybrid image
cv2.imshow('Hybrid Image', hybrid_image)
cv2.waitKey(0)
cv2.destroyAllWindows()