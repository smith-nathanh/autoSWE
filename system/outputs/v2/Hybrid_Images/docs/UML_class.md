classDiagram
    class ImageProcessor {
        +applyGaussianBlur(image, sigma, kernelSize)
        +applyLowPassFilter(image)
        +applyHighPassFilter(image)
        +crossCorrelate(image1, image2)
        +convolve(image1, image2)
    }
    class HybridImageCreator {
        +createHybridImage(image1, image2, mixRatio, filterType1, filterType2)
    }
    class Image {
        +data
        +loadImage(filePath)
        +saveImage(filePath)
    }
    ImageProcessor --> Image
    HybridImageCreator --> ImageProcessor
    HybridImageCreator --> Image