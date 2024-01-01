import pytest
from src.doc_oct.docstring_parser import DocstringParser
import tempfile
import os

# Fixture to create a temporary Python file
@pytest.fixture
def temp_python_file():
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.py', delete=False) as tmp:
        yield tmp.name
        os.remove(tmp.name)

def test_get_docstring_no_docstring(temp_python_file):
    """
    Test get_docstring method with a file that does not have a docstring.
    """
    parser = DocstringParser()
    # Create a temporary file without a docstring
    with open(temp_python_file, 'w') as file:
        file.write("def test_function():\n    pass\n")

    # Test
    assert parser.get_docstring(temp_python_file) is None

def test_get_docstring_with_docstring(temp_python_file):
    """
    Test get_docstring method with a file that has a docstring.
    """
    parser = DocstringParser()
    # Create a temporary file with a docstring
    docstring = '"""This is a test docstring."""'
    with open(temp_python_file, 'w') as file:
        file.write(docstring + "\ndef test_function():\n    pass\n")

    # Test
    assert parser.get_docstring(temp_python_file) == "This is a test docstring."
