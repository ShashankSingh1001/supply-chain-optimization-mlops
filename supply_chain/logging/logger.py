import logging
import os
from datetime import datetime

# Create logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Create log file with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Create a logger
project_logger = logging.getLogger("supply_chain_logger")
project_logger.setLevel(logging.INFO)

# Prevent duplicate logs if multiple imports happen
if not project_logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE_PATH, mode="a", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    project_logger.addHandler(file_handler)

# Stop logs from propagating to root logger
project_logger.propagate = False

# Initial entry
project_logger.info("[INIT] Logger file created")

# Export path so tests and other modules can access it
__all__ = ["project_logger", "LOG_FILE_PATH"]
