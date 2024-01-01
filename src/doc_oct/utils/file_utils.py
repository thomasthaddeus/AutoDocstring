import os

def read_file(file_path):
    """
    Reads the content of a given file.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The content of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """
    Writes content to a given file.

    Args:
        file_path (str): The path to the file to write.
        content (str): The content to write to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def append_to_file(file_path, content):
    """
    Appends content to the end of a given file.

    Args:
        file_path (str): The path to the file.
        content (str): The content to append.
    """
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)

def file_exists(file_path):
    """
    Checks if a file exists at a given path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(file_path)

# Additional utility functions can be added as needed, such as file deletion, copying, etc.
