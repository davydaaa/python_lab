"""Module providing the LackPenException class.

This module defines the LackPenException class, which is an exception raised when there
are not enough pens available.

Example:
    try:
        # Some code that may raise the LackPenException
        raise LackPenException()
    except LackPenException as e:
        print(e)

Attributes:
    None


"""


class LackPenException(Exception):
    """Exception raised when there are not enough pens available.

    Attributes:
        message (str): A static class attribute containing the default error message.
    """

    message = "Not enough pens"

    def __init__(self):
        """Initialize the LackPenException.

        The LackPenException is raised when there are not enough pens available.

        Args:
            None

        Returns:
            None
        """
        super().__init__(self.message)
