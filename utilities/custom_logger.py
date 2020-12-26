import inspect
import logging
import os
import time


def custom_logger(level=logging.INFO):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    file_name = "log_" + str(round(time.time() * 1000)) + ".log"
    root = os.path.dirname(os.path.dirname(__file__))
    logger_path = os.path.join(root, "logs", file_name)
    file_handler = logging.FileHandler(logger_path, mode="w")
    file_handler.setLevel(level)

    formatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s",
                                  datefmt="%d/%m/%Y %H:%M:%S")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger