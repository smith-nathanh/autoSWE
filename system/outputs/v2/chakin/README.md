# Chakin Project

The `chakin` project is a tool designed to streamline the process of downloading pre-trained word vectors, which are essential components in natural language processing (NLP) tasks. This tool simplifies the retrieval process, eliminating the need for manual searches and downloads, thereby saving time and reducing complexity.

## Features
- **Easy Installation**: Install `chakin` with a simple pip command.
- **Search Functionality**: Search for word vectors by language.
- **Download Functionality**: Download word vectors by specifying either a numerical index or a name.
- **Progress Tracking**: Visual progress bar for download tracking.

## Installation

To install `chakin`, use pip:

```bash
pip install chakin
```

## Usage

### Search for Word Vectors

To search for available word vectors by language:

```bash
python -c "import chakin; print(chakin.search(lang='English'))"
```

### Download Word Vectors

To download a specific word vector:

```bash
python -c "import chakin; chakin.download(number=2, save_dir='./')"
```

## Requirements

- Python
- pandas
- progressbar2
- six

## Project Structure

- `chakin/`: Contains the main library code.
- `tests/`: Contains unit tests.
- `examples/`: Contains example scripts for using `chakin`.

## License

This project is licensed under the MIT License.