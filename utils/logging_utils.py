import logging

# Set up a logger for the project
def setup_logger(name="selenium_test_logger", log_file="test_log.log", level=logging.INFO):
    """Set up the logger for the test automation project."""
    logger = logging.getLogger(name)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
