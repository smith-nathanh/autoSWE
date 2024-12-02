# Chakin

Chakin is a Python library designed to streamline the process of downloading pre-trained word vectors, which are essential components in natural language processing (NLP) tasks. This tool simplifies the retrieval process, saving time and reducing complexity for researchers and developers.

## Features
- **Easy Installation**: Install via pip.
- **Search Functionality**: Search for word vectors by language.
- **Download Functionality**: Download word vectors by specifying a numerical index or name.
- **Progress Tracking**: Visual progress bar for downloads.

## Installation

```bash
pip install chakin
```

## Usage

### Search for Word Vectors

```python
import chakin
print(chakin.search(lang='English'))
```

### Download Word Vectors

```python
import chakin
chakin.download(number=2, save_dir='./')
```

## Requirements
- Python
- pandas
- progressbar2
- six

## License
MIT License