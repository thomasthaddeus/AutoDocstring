"""main.py

Implements the main functions of the doc_oct library

_extended_summary_
"""

import argparse
import  logging
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
    writer = DocstringWriter()
    dry_run_writer = DryRunWriter(logger, parser, writer) if dry_run else writer

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
        except (TypeError, ValueError) as e:
            logger.log(f"Error processing file: {file_path}, Error: {str(e)}", level=logging.ERROR)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the doc_oct script to update docstrings.")
    parser.add_argument("directory", help="Directory to scan for Python files")
    parser.add_argument("--dry-run", action="store_true", help="Run in dry-run mode")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")

    args = parser.parse_args()
    main(args.directory, dry_run=args.dry_run, interactive=args.interactive)
