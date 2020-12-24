import logging
import os


class LogGenerator:

    @staticmethod
    def loggen():

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler('./reports/base_report.log')
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger
