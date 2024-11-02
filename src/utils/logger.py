import logging
import os

def setup_logger(name: str, log_file: str, level=logging.INFO):
    """Set up a logger with a specified name and log file."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create a file handler
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    
    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger('example_logger', 'logs/example.log')
    logger.info("Logger is set up and ready to use.")
