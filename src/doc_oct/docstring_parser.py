"""docstring_parser.py

Parses Python files to find and analyze docstrings of modules, classes, and functions.
"""

import ast

class DocstringParser:
    """Parses Python files for docstrings."""

    def __init__(self):
        """Initializes a new DocstringParser."""
        pass

    def get_docstring(self, file_path):
        """
        Parses a Python file and returns docstrings for modules, classes, and functions.

        Args:
            file_path (str): The path to the Python file.

        Returns:
            dict: A dictionary containing docstrings keyed by their type ('module', 'class', 'function') and name.
        """
        docstrings = {'module': None, 'classes': {}, 'functions': {}}
        with open(file=file_path, mode='r', encoding='utf-8') as f:
            module = ast.parse(f.read())
            docstrings['module'] = ast.get_docstring(module)

            for node in ast.walk(module):
                if isinstance(node, ast.ClassDef):
                    docstrings['classes'][node.name] = ast.get_docstring(node)
                elif isinstance(node, ast.FunctionDef):
                    docstrings['functions'][node.name] = ast.get_docstring(node)

        return docstrings
