import os
import logging
from supply_chain.logging.logger import LOG_FILE_PATH, project_logger

def test_logger_file_created():
    project_logger.info("Testing logger file creation")
    assert os.path.exists(LOG_FILE_PATH)

def test_logger_write_entry():
    test_msg = "This is a test log entry."
    project_logger.info(test_msg)
    for handler in project_logger.handlers:
        handler.flush()
    with open(LOG_FILE_PATH, 'r') as f:
            logs = f.read()

    assert test_msg in logs