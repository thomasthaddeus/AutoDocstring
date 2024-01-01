"""docstring_writer.py

Provides functionality to write and update docstrings in Python files.
"""

import ast
import astunparse  # Using astunparse for converting AST back to source code

class DocstringWriter:
    """Writes and updates docstrings in Python files."""

    def __init__(self):
        """Initializes a new DocstringWriter."""
        pass

    def write_docstring(self, file_path, new_docstring):
        """
        Writes or updates a docstring in a Python file.

        Args:
            file_path (str): The path to the Python file.
            new_docstring (str): The docstring to write or update.
        """
        with open(file=file_path, mode='r+', encoding='utf-8') as file:
            source = file.read()
            root = ast.parse(source)

            if not ast.get_docstring(root):
                # No existing docstring, write new one
                file.seek(0, 0)
                file.write('"""' + new_docstring.strip() + '"""\n' + source)
            else:
                # Update existing docstring
                if isinstance(root.body[0], ast.Expr) and isinstance(root.body[0].value, ast.Str):
                    root.body[0].value = ast.Str(s=new_docstring.strip())
                else:
                    # Handle cases where the first expression isn't a docstring
                    root.body.insert(0, ast.Expr(value=ast.Str(s=new_docstring.strip())))

                updated_source = astunparse.unparse(root)
                file.seek(0, 0)
                file.write(updated_source)
