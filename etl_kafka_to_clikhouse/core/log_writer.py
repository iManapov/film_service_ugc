import logging.config

from config import LoggerSettings


LOGGING_CONFIG = LoggerSettings().dict()
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("my_logger")


if __name__ == "__main__":
    logger.debug("test logging")
