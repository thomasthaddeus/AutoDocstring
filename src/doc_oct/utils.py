"""utils.py

_summary_

_extended_summary_
"""

import os
import shutil

def scan_directory(directory):
    """
    Returns a list of all Python files in a directory.

    Args:
        directory (str): The directory to scan.

    Returns:
        list[str]: A list of Python file paths.
    """
    return [os.path.join(root, file)
            for root, dirs, files in os.walk(directory)
            for file in files if file.endswith('.py')]

def backup_file(file_path):
    """
    Creates a backup of a file.

    Args:
        file_path (str): The path to the file to backup.
    """
    shutil.copyfile(file_path, file_path + '.bak')
