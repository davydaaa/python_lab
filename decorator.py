import logging
from functools import wraps


class LackPenException(Exception):
    pass


def logged(exception, mode):
    """Decorator that logs exceptions raised by the decorated function.

    Args:
        exception (Exception): The exception type to be caught and logged.
        mode (str): The mode of logging. Can be "console" or "file".

    Raises:
        ValueError: If an invalid mode is provided.

    Returns:
        function: The decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger()
                if mode == "console":
                    logger.addHandler(logging.StreamHandler())
                elif mode == "file":
                    logger.addHandler(logging.FileHandler("log.txt"))
                else:
                    raise ValueError("Invalid login mode")

                logger.exception(e)

        return wrapper

    return decorator
