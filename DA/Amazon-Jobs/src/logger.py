import logging
import os
import yaml

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(PROJECT_DIR, "config.yml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)
    LOG_DIR = os.path.join(PROJECT_DIR, config["logging"]["log_dir"])  
    LOG_FILE = os.path.join(LOG_DIR, config["logging"]["log_file"]) 
    f.close()

LOG_DIR = os.path.join(PROJECT_DIR, LOG_DIR)
LOG_FILE = os.path.join(LOG_DIR, LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",  
    handlers=[
        logging.FileHandler(LOG_FILE, mode='a'), 
        logging.StreamHandler()  
    ]
)

def get_logger(name: str) -> logging.Logger:
    """Creates and returns a logger with the given name."""
    return logging.getLogger(name)

# Example usage
if __name__ == "__main__":
    logger = get_logger("example_logger")
    logger.info("This is an info message.")
    logger.error("This is an error message.")
