import pytest
from unittest.mock import Mock
from src.doc_oct.dry_run import DryRunWriter
from src.doc_oct.docstring_parser import DocstringParser
from src.doc_oct.docstring_writer import DocstringWriter

def test_dry_run_write_new_docstring():
    """
    Test DryRunWriter for simulating writing a new docstring.
    """
    logger = Mock()
    parser = Mock()
    writer = Mock()

    # Simulate no existing docstring
    parser.get_docstring.return_value = None

    dry_run_writer = DryRunWriter(logger, parser, writer)
    file_path = 'test_file.py'
    new_docstring = '"""This is a new docstring."""'

    # Perform dry run write
    dry_run_writer.write_docstring(file_path, new_docstring)

    # Assert logger was called with the correct message
    logger.log.assert_called_with(f"Would write the following docstring to {file_path}:\n{new_docstring}")

def test_dry_run_update_existing_docstring():
    """
    Test DryRunWriter for simulating updating an existing docstring.
    """
    logger = Mock()
    parser = Mock()
    writer = Mock()

    # Simulate existing docstring
    parser.get_docstring.return_value = '"""Original docstring."""'

    dry_run_writer = DryRunWriter(logger, parser, writer)
    file_path = 'test_file.py'
    updated_docstring = '"""Updated docstring."""'

    # Perform dry run update
    dry_run_writer.write_docstring(file_path, updated_docstring)

    # Assert logger was called with the correct message
    logger.log.assert_called_with(f"Would write the following docstring to {file_path}:\n{updated_docstring}")
