import cv2
import numpy as np
from src.image import Image
from src.hybrid_image_creator import HybridImageCreator

# Load images
image1 = Image.load_image('path/to/image1.jpg')
image2 = Image.load_image('path/to/image2.jpg')

# Create hybrid image
creator = HybridImageCreator()
hybrid_image = creator.create_hybrid_image(image1, image2, mix_ratio=0.5, filter_type1='low', filter_type2='high')

# Save and display hybrid image
Image.save_image(hybrid_image, 'path/to/hybrid_image.jpg')
cv2.imshow('Hybrid Image', hybrid_image)
cv2.waitKey(0)
cv2.destroyAllWindows()