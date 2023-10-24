"""main.py

Implements the main functions of the doc_oct library

_extended_summary_
"""

from doc_oct.docstring_parser import DocstringParser
from doc_oct.docstring_writer import DocstringWriter
from doc_oct.dry_run import DryRunWriter
from doc_oct.logger import Logger
from doc_oct.utils import scan_directory, backup_file

def prompt_for_confirmation(message):
    """Prompts the user for confirmation before proceeding."""
    while True:
        response = input(message + ' (y/n) ').lower()
        if response in ['y', 'n']:
            return response == 'y'
        print('Invalid response. Please enter y or n.')


def main(directory, dry_run=False, interactive=False):
    """Scans a directory and adds docstrings to Python files as necessary."""
    logger = Logger('/logs/logs.txt')
    parser = DocstringParser()
    writer = DryRunWriter(logger) if dry_run else DocstringWriter()

    for file_path in scan_directory(directory):
        try:
            logger.log(f"Processing file: {file_path}")
            docstring = parser.get_docstring(file_path)
            if docstring is None:
                logger.log(f"No docstring found in {file_path}, adding one...")
                if interactive and not prompt_for_confirmation(f'Add docstring to {file_path}?'):
                    continue
                if not dry_run:
                    backup_file(file_path)
                writer.write_docstring(file_path, '"""\nYour docstring here.\n"""')
        except Exception as e:
            logger.log(f"Error processing file: {file_path}, Error: {str(e)}", level=logging.ERROR)

if __name__ == "__main__":
    main("path_to_your_directory", dry_run=True, interactive=True)
