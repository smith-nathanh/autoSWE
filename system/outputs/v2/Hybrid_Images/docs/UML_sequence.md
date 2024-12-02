sequenceDiagram
    participant User
    participant DemoScript
    participant HybridImageCreator
    participant ImageProcessor
    participant Image
    User->>DemoScript: Run demo.py
    DemoScript->>HybridImageCreator: createHybridImage(image1, image2, mixRatio, filterType1, filterType2)
    HybridImageCreator->>Image: loadImage(filePath1)
    HybridImageCreator->>Image: loadImage(filePath2)
    HybridImageCreator->>ImageProcessor: applyLowPassFilter(image1)
    HybridImageCreator->>ImageProcessor: applyHighPassFilter(image2)
    ImageProcessor->>Image: saveImage(filePath)
    HybridImageCreator->>Image: saveImage(hybridImagePath)
    Image-->>User: Display hybrid image