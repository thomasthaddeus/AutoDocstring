# AutoDocstring

AutoDocstring is a Python tool designed for automatic generation and updating of Python docstrings in the Google style. It simplifies the process of maintaining consistent and comprehensive documentation in Python codebases.

## Features

- Scans Python files in a given directory (including subdirectories) for docstrings.
- Automatically adds or updates docstrings in Google style.
- Supports dry-run mode to preview changes without modifying files.
- Provides options for interactive updates and file backup.

## Requirements

- Python 3.8 or higher

## Installation

Clone the repository and install the dependencies using Poetry:

```bash
git clone https://github.com/thomasthaddeus/AutoDocstring.git
cd AutoDocstring
poetry install
```

## Usage

Run the tool from the command line:

```bash
poetry run python src/main.py [directory] [--dry-run] [--interactive]
```

Arguments:

- `directory`: Path to the directory containing Python files to process.
- `--dry-run`: Preview changes without modifying files.
- `--interactive`: Interactive mode for manual confirmation of each change.

## Documentation

For more detailed information about the tool, refer to the documentation in the `docs` directory.

## Contributing

Contributions to the AutoDocstring project are welcome! Please refer to the `CONTRIBUTING.md` file for guidelines on how to contribute.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

For any queries or suggestions, feel free to contact the maintainers at [thaddeus.r.thomas@gmail.com].

---

© 2023 [Thaddeus Thomas] - All Rights Reserved
