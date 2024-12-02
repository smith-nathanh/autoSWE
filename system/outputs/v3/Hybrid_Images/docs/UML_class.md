classDiagram
    class ImageProcessor {
        +apply_low_pass_filter(image, sigma, kernel_size)
        +apply_high_pass_filter(image, sigma, kernel_size)
        +apply_gaussian_blur(image, sigma, kernel_size)
        +cross_correlation(image1, image2)
        +convolution(image1, image2)
    }
    class HybridImageCreator {
        +create_hybrid_image(image1, image2, mix_ratio, filter_type1, filter_type2)
    }
    class Main {
        +main()
    }
    ImageProcessor <|-- HybridImageCreator
    Main --> HybridImageCreator