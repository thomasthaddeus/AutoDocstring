"""docstring_writer.py

_summary_

_extended_summary_
"""


class DocstringWriter:
    """Writes Google-style docstrings to a Python file."""

    def __init__(self):
        """Initializes a new DocstringWriter."""
        pass

    def write_docstring(self, file_path, docstring):
        """
        Writes a docstring to a Python file.

        Args:
            file_path (str): The path to the Python file.
            docstring (str): The docstring to write.
        """
        with open(file=file_path, mode='r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(docstring.strip() + '\n' + content)
