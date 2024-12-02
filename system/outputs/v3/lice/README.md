# Lice Project

The `lice` project is a command-line tool designed to streamline the creation of license files for software projects. It automates the retrieval and formatting of various open-source licenses, making it easier for developers to comply with legal requirements and share their code with the appropriate licensing.

## Features
- **License Generation**: Generate licenses such as BSD-3, MIT, GPL, etc., with simple commands.
- **Customization**: Specify the year and organization for the generated license.
- **Integration**: Uses `git config` or the `$USER` environment variable if the organization is not specified.
- **Formatting**: Create license headers for source files in different programming languages.
- **File Creation**: Generate a new source file with the license commented in the header.
- **Language Detection**: Automatically detect the language for file formatting based on the file extension provided.
- **Extensibility**: Add support for additional licenses or programming languages.

## Installation

To install the `lice` tool, clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd project-root
```

## Usage

Here are some example commands to use `lice`:

```bash
# Generate a BSD3 license using default options
python lice/core.py bsd3

# Generate an MIT license using default options
python lice/core.py mit

# Generate a GPL3 license for the year 2021 and organization 'ExampleOrg'
python lice/core.py gpl3 --year 2021 --org 'ExampleOrg'

# Generate an Apache license with a header formatted for a Python source file
python lice/core.py apache --header --language py

# Generate a BSD2 license and save it to a file named 'LICENSE'
python lice/core.py bsd2 --file LICENSE
```

## Dependencies

- Python
- pytest
- flake8

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License.