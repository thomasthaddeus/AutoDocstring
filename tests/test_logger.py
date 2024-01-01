import pytest
import logging
from doc_oct.logger import Logger
from unittest.mock import Mock, patch

def test_logger_info_logging():
    """
    Test that the Logger logs an info message correctly.
    """
    with patch('logging.Logger.info') as mock_info_log:
        logger = Logger('/fake/log/path.txt')
        logger.info("Test info message")
        mock_info_log.assert_called_once_with("Test info message")

def test_logger_error_logging():
    """
    Test that the Logger logs an error message correctly.
    """
    with patch('logging.Logger.error') as mock_error_log:
        logger = Logger('/fake/log/path.txt')
        logger.error("Test error message")
        mock_error_log.assert_called_once_with("Test error message")

def test_logger_debug_logging():
    """
    Test that the Logger logs a debug message correctly.
    """
    with patch('logging.Logger.debug') as mock_debug_log:
        logger = Logger('/fake/log/path.txt')
        logger.debug("Test debug message")
        mock_debug_log.assert_called_once_with("Test debug message")
