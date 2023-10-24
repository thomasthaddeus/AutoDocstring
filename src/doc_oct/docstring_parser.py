"""docstring_parser.py

_summary_

_extended_summary_
"""


import ast

class DocstringParser:
    """Parses Python files to find and analyze docstrings."""

    def __init__(self):
        """Initializes a new DocstringParser."""
        pass

    def get_docstring(self, file_path):
        """
        Returns the docstring of a Python file.

        Args:
            file_path (str): The path to the Python file.

        Returns:
            str: The docstring, or None if the file does not have a docstring.
        """
        with open(file=file_path, mode='r', encoding='utf-8') as f:
            module = ast.parse(f.read())
            return ast.get_docstring(module)
