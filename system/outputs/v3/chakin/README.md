# Chakin

Chakin is a Python library designed to streamline the process of downloading pre-trained word vectors, which are essential components in natural language processing (NLP) tasks. The library provides an efficient, user-friendly tool to download pre-trained word vectors, supporting NLP applications by making a wide range of word vectors easily accessible.

## Features
- **Easy Installation**: Install with a simple pip command.
- **Search Functionality**: Search for word vectors by language.
- **Download Functionality**: Download word vectors by specifying either a numerical index or a name.
- **Progress Tracking**: Visual progress bar for download tracking.

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

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
