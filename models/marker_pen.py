"""
This module provides classes for managing marker pens and calculating their prices.
"""
from models.school_pen import Pen

# pylint: disable=too-few-public-methods


class MarkerPen(Pen):
    """
    Concrete subclass representing a marker pen.
    """
    PRICE_PER_MARKER = 3.0

    def calculate_price(self):
        """
        Calculates the total price of the marker pen.

        :return: The total price of the marker pen.
        """
        return self.num_pens * self.PRICE_PER_MARKER


