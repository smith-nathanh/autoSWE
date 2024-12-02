#!/bin/bash

echo "Searching for English word vectors..."
python -c "import chakin; print(chakin.search(lang='English'))"

echo "Downloading the fastText English word vector..."
python -c "import chakin; chakin.download(number=2, save_dir='./')"