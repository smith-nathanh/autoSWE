from src.image_processor import ImageProcessor

class HybridImageCreator:
    def create_hybrid_image(self, image1, image2, mix_ratio, filter_type1, filter_type2):
        if filter_type1 == 'low':
            image1 = ImageProcessor.apply_low_pass_filter(image1, sigma=5, kernel_size=15)
        elif filter_type1 == 'high':
            image1 = ImageProcessor.apply_high_pass_filter(image1, sigma=5, kernel_size=15)

        if filter_type2 == 'low':
            image2 = ImageProcessor.apply_low_pass_filter(image2, sigma=5, kernel_size=15)
        elif filter_type2 == 'high':
            image2 = ImageProcessor.apply_high_pass_filter(image2, sigma=5, kernel_size=15)

        hybrid_image = cv2.addWeighted(image1, mix_ratio, image2, 1 - mix_ratio, 0)
        return hybrid_image