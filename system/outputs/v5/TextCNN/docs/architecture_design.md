project-root/
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── model/
│   │   ├── __init__.py
│   │   └── text_cnn.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_loader.py
│   ├── training/
│   │   ├── __init__.py
│   │   ├── trainer.py
│   │   └── checkpoint_manager.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── examples/
│   ├── example_usage.sh
│   └── example_training.py
└── tests/
    ├── __init__.py
    ├── test_data_loader.py
    ├── test_text_cnn.py
    ├── test_trainer.py
    └── test_checkpoint_manager.py