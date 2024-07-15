# logger.py

import logging
import os
from logging.handlers import TimedRotatingFileHandler

class MaxLevelFilter(logging.Filter):
    def __init__(self, max_level):
        self.max_level = max_level
        super(MaxLevelFilter, self).__init__()

    def filter(self, record):
        return record.levelno <= self.max_level

class LoggerManager:
    
    def __init__(self, log_dir=None, logger_name='default', log_error_file=None):
        """
        Initialize the LoggerManager with a log directory.
        :param log_dir: Directory where log files will be stored.
        :param log_name: Name of the logger to be used.
        :param log_error_file: Name of the error log file to be used.
        """
        
        self.log_dir = log_dir if log_dir else 'logs'
        self.logger_name = logger_name
        self.log_error_file = log_error_file if log_error_file else "{}_error.log".format(logger_name)
        self.create_log_directory()


    def create_log_directory(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)


    def get_logger(self):
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)

        log_file = os.path.join(self.log_dir, "{}.log".format(self.logger_name))
        log_error_file = os.path.join(self.log_dir, self.log_error_file)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        file_handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1)
        file_handler.suffix = "%Y-%m-%d"
        file_handler.setLevel(logging.DEBUG)
        file_handler.addFilter(MaxLevelFilter(logging.WARNING))

        error_file_handler = TimedRotatingFileHandler(log_error_file, when="midnight", interval=1)
        error_file_handler.suffix = "%Y-%m-%d"
        error_file_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        error_file_handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
            logger.addHandler(error_file_handler)

        return logger


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logger = LoggerManager(logger_name='cron_presico').get_logger()
            logger.error("Ha ocurrido un error: {}".format(err))
    return wrapper



if __name__ == "__main__":
    logger_manager = LoggerManager(logger_name='cron_presico')
    logger = logger_manager.get_logger()
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
