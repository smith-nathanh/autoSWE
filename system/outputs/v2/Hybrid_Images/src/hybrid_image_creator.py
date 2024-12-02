from src.image_processor import ImageProcessor

class HybridImageCreator:
    def createHybridImage(self, image1, image2, mixRatio, filterType1, filterType2):
        processor = ImageProcessor()

        if filterType1 == 'low':
            image1 = processor.applyLowPassFilter(image1)
        elif filterType1 == 'high':
            image1 = processor.applyHighPassFilter(image1)

        if filterType2 == 'low':
            image2 = processor.applyLowPassFilter(image2)
        elif filterType2 == 'high':
            image2 = processor.applyHighPassFilter(image2)

        hybrid_image = cv2.addWeighted(image1, mixRatio, image2, 1 - mixRatio, 0)
        return hybrid_image