import logging
import sys

from app.shared.utils import get_config


__all__ = [
    'get_logger',
]


def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        out = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s \
            - %(module)s - %(message)s'
        )
        out.setFormatter(formatter)
        logger.addHandler(out)
        logger.setLevel(get_config('LOGGING_LEVEL'))
        logger.propagate = False
    return logger
