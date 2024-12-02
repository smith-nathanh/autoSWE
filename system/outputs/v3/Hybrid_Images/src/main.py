from src.hybrid_image_creator import HybridImageCreator
import cv2

if __name__ == '__main__':
    # Load images
    image1 = cv2.imread('examples/sample_images/image1.jpg', cv2.IMREAD_COLOR)
    image2 = cv2.imread('examples/sample_images/image2.jpg', cv2.IMREAD_COLOR)

    # Parameters
    mix_ratio = 0.5
    filter_type1 = 'low'
    filter_type2 = 'high'

    # Create hybrid image
    creator = HybridImageCreator()
    hybrid_image = creator.create_hybrid_image(image1, image2, mix_ratio, filter_type1, filter_type2)

    # Display result
    cv2.imshow('Hybrid Image', hybrid_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()