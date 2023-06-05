import logging


class LackPenException(Exception):
    pass


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger(func.__module__)
                logger.setLevel(logging.DEBUG)

                if mode == "console":
                    handler = logging.StreamHandler()
                elif mode == "file":
                    handler = logging.FileHandler("log.txt")
                else:
                    raise ValueError(f"Invalid mode: {mode}") from e

                logger.addHandler(handler)
                logger.exception(e)

        return wrapper

    return decorator
