from logging import getLogger
from logging import FileHandler
from logging import Formatter
from logging import DEBUG


def create_logger(name: str, output_file: str):
    logger = getLogger(name)
    handler = FileHandler(output_file)

    formatter = \
        Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            '%Y-%m-%d %H:%M:%S'
        )
    handler.setFormatter(formatter)

    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)

    logger.addHandler(handler)
    logger.propagate = False
    return logger
