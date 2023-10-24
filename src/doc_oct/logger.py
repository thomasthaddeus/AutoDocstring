"""logger.py

_summary_

_extended_summary_
"""

import logging

class Logger:
    """Logs operations to a text file and the console."""

    def __init__(self, log_file):
        """
        Initializes a new Logger.

        Args:
            log_file (str): The path to the log file.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log(self, message, level=logging.INFO):
        """
        Logs a message.

        Args:
            message (str): The message to log.
            level (int): The log level.
        """
        self.logger.log(level, message)
