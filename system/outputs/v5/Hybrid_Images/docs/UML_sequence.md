sequenceDiagram
    participant User
    participant DemoScript
    participant HybridImageCreator
    participant ImageProcessor

    User->>DemoScript: Run demo.py
    DemoScript->>HybridImageCreator: create_hybrid_image(image1, image2, mix_ratio, filter_type1, filter_type2)
    HybridImageCreator->>ImageProcessor: apply_low_pass_filter(image1, sigma, kernel_size)
    ImageProcessor-->>HybridImageCreator: low_pass_image1
    HybridImageCreator->>ImageProcessor: apply_high_pass_filter(image2, sigma, kernel_size)
    ImageProcessor-->>HybridImageCreator: high_pass_image2
    HybridImageCreator->>HybridImageCreator: combine_images(low_pass_image1, high_pass_image2, mix_ratio)
    HybridImageCreator-->>DemoScript: hybrid_image
    DemoScript-->>User: Display hybrid_image