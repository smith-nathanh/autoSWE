#!/bin/bash

# Example usage of the hybrid image creator

python -c "
from src.image import Image
from src.hybrid_image_creator import HybridImageCreator

# Load images
image1 = Image.load_image('examples/image1.jpg')
image2 = Image.load_image('examples/image2.jpg')

# Create hybrid image
creator = HybridImageCreator()
hybrid_image = creator.create_hybrid_image(image1, image2, 0.5, 'low', 'high', 5, 15)

# Save hybrid image
Image.save_image(hybrid_image, 'examples/hybrid_image.jpg')
"
