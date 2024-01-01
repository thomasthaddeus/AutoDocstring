"""utils.py

Provides various utility functions for the application.
"""

import os
import shutil
import json

def scan_directory(directory):
    """
    Returns a list of all Python files in a directory.

    Args:
        directory (str): The directory to scan.

    Returns:
        list[str]: A list of Python file paths.
    """
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    return py_files

def backup_file(file_path):
    """
    Creates a backup of a file.

    Args:
        file_path (str): The path to the file to backup.
    """
    shutil.copyfile(file_path, file_path + '.bak')

def load_config(config_file):
    """
    Loads a configuration from a JSON file.

    Args:
        config_file (str): The path to the configuration file.

    Returns:
        dict: The configuration dictionary.
    """
    with open(config_file, 'r') as f:
        return json.load(f)

def save_config(config, config_file):
    """
    Saves a configuration to a JSON file.

    Args:
        config (dict): The configuration dictionary.
        config_file (str): The path to the configuration file.
    """
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)
