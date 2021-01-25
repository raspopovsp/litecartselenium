import inspect
import logging
import os


class LogGenerator:

    @staticmethod
    def loggen():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler('./reports/base_report.log')
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger
