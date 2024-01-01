import pytest
from src.doc_oct.utils import scan_directory, backup_file
import tempfile
import os
import shutil

def create_test_directory_with_files():
    """
    Helper function to create a test directory with Python files.
    Returns the path of the test directory.
    """
    test_dir = tempfile.mkdtemp()
    file_paths = []
    for i in range(3):
        file_path = os.path.join(test_dir, f'test_file_{i}.py')
        with open(file_path, 'w') as f:
            f.write(f'# Test file {i}')
        file_paths.append(file_path)
    return test_dir, file_paths

def test_scan_directory():
    """
    Test scan_directory function for correctly listing Python files in a directory.
    """
    test_dir, expected_files = create_test_directory_with_files()
    found_files = scan_directory(test_dir)

    # Clean up
    shutil.rmtree(test_dir)

    # Check if all files were found
    assert set(found_files) == set(expected_files)

def test_backup_file():
    """
    Test backup_file function for correctly creating a backup of a file.
    """
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.py', delete=False) as tmp:
        file_path = tmp.name
        backup_file(file_path)
        backup_path = file_path + '.bak'

    # Check if backup file exists
    assert os.path.exists(backup_path)

    # Clean up
    os.remove(file_path)
    os.remove(backup_path)
