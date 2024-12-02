# Chakin Project

The `chakin` project is a tool designed to simplify the process of downloading pre-trained word vectors for natural language processing (NLP) tasks. It provides a command-line interface for searching and downloading word vectors by language, with progress tracking.

## Features
- Easy installation via pip.
- Search for word vectors by language.
- Download word vectors by specifying a numerical index or name.
- Visual progress tracking during downloads.

## Installation
To install `chakin`, use pip:
```bash
pip install chakin
```

## Usage
Search for word vectors:
```bash
python -c "import chakin; print(chakin.search(lang='English'))"
```

Download a word vector:
```bash
python -c "import chakin; chakin.download(number=2, save_dir='./')"
```

## Requirements
- Python
- pandas
- progressbar2
- six

## License
This project is licensed under the MIT License.