"""logger.py

Provides logging functionality for the application.
"""

import logging

class Logger:
    """Logs operations to a text file and the console."""

    def __init__(self, log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'):
        """
        Initializes a new Logger.

        Args:
            log_file (str): The path to the log file.
            level (int): The log level.
            format (str): The log format.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        formatter = logging.Formatter(format)

        # File handler for logging to a file
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        # Stream handler for logging to the console
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log(self, message, level=logging.INFO):
        """
        Logs a message at the specified log level.

        Args:
            message (str): The message to log.
            level (int): The log level.
        """
        self.logger.log(level, message)

    def error(self, message):
        """Logs an error message."""
        self.logger.error(message)

    def warning(self, message):
        """Logs a warning message."""
        self.logger.warning(message)

    def debug(self, message):
        """Logs a debug message."""
        self.logger.debug(message)

    def info(self, message):
        """Logs an info message."""
        self.logger.info(message)
