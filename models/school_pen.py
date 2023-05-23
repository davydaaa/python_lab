"""
This module provides classes for managing school pens and calculating their prices.
"""
from models.pen import Pen

# pylint: disable=too-few-public-methods


class SchoolPen(Pen):
    """
    Concrete subclass representing a school pen.
    """
    PRICE_PER_PENCIL = 1.0
    PRICE_PER_PEN = 2.0
    PRICE_PER_ERASER = 0.5

    def calculate_price(self):
        """
        Calculates the total price of the school pen.

        :return: The total price of the school pen.
        """
        pencil_cost = self.num_pencils * self.PRICE_PER_PENCIL
        pen_cost = self.num_pens * self.PRICE_PER_PEN
        eraser_cost = self.num_erasers * self.PRICE_PER_ERASER
        return pencil_cost + pen_cost + eraser_cost
