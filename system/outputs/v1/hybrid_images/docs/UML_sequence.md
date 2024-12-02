sequenceDiagram
    participant User
    participant DemoScript
    participant HybridImageCreator
    participant ImageProcessor
    participant Image

    User->>DemoScript: Run demo.py
    DemoScript->>Image: Load image1
    DemoScript->>Image: Load image2
    DemoScript->>HybridImageCreator: create_hybrid_image(image1, image2, mix_ratio, filter_type1, filter_type2)
    HybridImageCreator->>ImageProcessor: apply_low_pass_filter(image1, sigma, kernel_size)
    HybridImageCreator->>ImageProcessor: apply_high_pass_filter(image2, sigma, kernel_size)
    ImageProcessor->>Image: Processed image1
    ImageProcessor->>Image: Processed image2
    HybridImageCreator->>Image: Save hybrid image
    Image-->>DemoScript: Hybrid image saved
    DemoScript-->>User: Display hybrid image