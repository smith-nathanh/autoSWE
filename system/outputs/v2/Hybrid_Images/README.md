# Hybrid Image Creator

## Introduction
This project is a Python-based application designed to create hybrid images by applying various image processing techniques. The application uses algorithms for cross-correlation, convolution, Gaussian blur, and high-pass and low-pass filters to manipulate images. The goal is to combine two images into a single hybrid image that exhibits properties of both source images at different viewing scales or distances.

## Features
- **Image Processing Operations**: Perform cross-correlation and convolution operations, apply Gaussian blur, and use low-pass and high-pass filters.
- **Hybrid Image Creation**: Combine two images into a hybrid image using specified mix ratios and filter types.

## Technical Requirements
- Python 3.x
- Libraries: NumPy, OpenCV

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd project_root
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To create a hybrid image, run the demo script:
```bash
python examples/demo.py
```

## Project Structure
- `examples/`: Contains example scripts and usage demonstrations.
- `src/`: Contains the source code for image processing and hybrid image creation.
- `tests/`: Contains unit tests for the application.

## License
This project is licensed under the MIT License.