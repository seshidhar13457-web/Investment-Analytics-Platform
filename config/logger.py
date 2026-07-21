import logging
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOG_FOLDER = PROJECT_ROOT / "logs"

LOG_FOLDER.mkdir(exist_ok=True)


def get_logger(name, log_file):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)


    if not logger.handlers:

        file_handler = logging.FileHandler(
            LOG_FOLDER / log_file
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)


    return logger