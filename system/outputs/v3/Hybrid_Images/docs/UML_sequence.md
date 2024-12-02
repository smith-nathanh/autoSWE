sequenceDiagram
    participant User
    participant Main
    participant HybridImageCreator
    participant ImageProcessor
    User->>Main: Run demo script
    Main->>HybridImageCreator: Initialize with images and parameters
    HybridImageCreator->>ImageProcessor: Apply low-pass filter to image1
    ImageProcessor-->>HybridImageCreator: Return low-pass filtered image1
    HybridImageCreator->>ImageProcessor: Apply high-pass filter to image2
    ImageProcessor-->>HybridImageCreator: Return high-pass filtered image2
    HybridImageCreator->>ImageProcessor: Apply Gaussian blur if needed
    ImageProcessor-->>HybridImageCreator: Return blurred image
    HybridImageCreator->>HybridImageCreator: Combine images into hybrid image
    HybridImageCreator-->>Main: Return hybrid image
    Main-->>User: Display hybrid image