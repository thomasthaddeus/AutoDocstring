import pytest
from src.doc_oct.docstring_writer import DocstringWriter
import tempfile
import os

# Fixture to create a temporary Python file
@pytest.fixture
def temp_python_file():
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.py', delete=False) as tmp:
        yield tmp.name
        os.remove(tmp.name)

def test_write_docstring_new(temp_python_file):
    """
    Test write_docstring method for a file that does not have a docstring.
    """
    writer = DocstringWriter()
    new_docstring = '"""This is a new docstring."""'

    # Write new docstring to the file
    writer.write_docstring(temp_python_file, new_docstring)

    # Read the file and assert the new docstring is written
    with open(temp_python_file, 'r') as file:
        content = file.read()
        assert new_docstring in content

def test_update_existing_docstring(temp_python_file):
    """
    Test write_docstring method for updating an existing docstring.
    """
    writer = DocstringWriter()
    original_docstring = '"""Original docstring."""'
    new_docstring = '"""Updated docstring."""'

    # Create a file with an existing docstring
    with open(temp_python_file, 'w') as file:
        file.write(original_docstring + "\ndef test_function():\n    pass\n")

    # Update the docstring
    writer.write_docstring(temp_python_file, new_docstring)

    # Read the file and assert the docstring is updated
    with open(temp_python_file, 'r') as file:
        content = file.read()
        assert new_docstring in content
        assert original_docstring not in content
