sequenceDiagram
    participant User
    participant Image
    participant ImageProcessor
    participant HybridImageCreator

    User->>Image: load_image(file_path1)
    User->>Image: load_image(file_path2)
    Image-->>User: image1, image2

    User->>HybridImageCreator: create_hybrid_image(image1, image2, mix_ratio, filter_type1, filter_type2)
    HybridImageCreator->>ImageProcessor: apply_low_pass_filter(image1, sigma, kernel_size)
    ImageProcessor-->>HybridImageCreator: low_pass_image1
    HybridImageCreator->>ImageProcessor: apply_high_pass_filter(image2, sigma, kernel_size)
    ImageProcessor-->>HybridImageCreator: high_pass_image2

    HybridImageCreator->>Image: save_image(hybrid_image_path)
    Image-->>User: hybrid_image