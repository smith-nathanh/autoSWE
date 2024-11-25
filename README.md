# autoSWE

autoSWE is a software engineering automation tool designed to produce a fully-functioning code repository based on a Produce Requirements Document (PRD). It produces the artifacts measured in [DevBench ](https://github.com/open-compass/DevBench), a software engineering benchmark designed to test the efficacy of LLM-based code generation systems.

For more detailed information on the features, tools, and processes used in autoSWE, please refer to the [system/README.md](system/README.md) document.

## Features

- Automated code generation from an input PRD.md file

## Deployment with Flask

autoSWE is deployed using Flask, a lightweight WSGI web application framework in Python. Flask makes it easy to set up a web server and handle HTTP requests.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/autoSWE.git
    cd autoSWE
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Flask App

To launch the Flask application, run the following command:
```bash
python main.py
```

This will start the Flask development server, and you can access the application by navigating to `http://127.0.0.1:5000` in your web browser.
