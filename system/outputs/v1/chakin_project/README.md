# Chakin Project

Chakin is a tool designed to streamline the process of downloading pre-trained word vectors for NLP tasks. It provides easy access to a variety of word vectors, allowing researchers and developers to enhance their language models efficiently.

## Features
- Easy installation via pip
- Search for word vectors by language
- Download word vectors by specifying a numerical index or name
- Visual progress tracking during downloads

## Installation
To install Chakin, simply run:
```
pip install -r requirements.txt
```

## Usage
To search for word vectors in English:
```
python -c "import chakin; print(chakin.search(lang='English'))"
```

To download a specific word vector:
```
python -c "import chakin; chakin.download(number=2, save_dir='./')"
```

## Testing
To run tests, use:
```
python -m unittest discover -s tests
```

## License
This project is licensed under the MIT License.
