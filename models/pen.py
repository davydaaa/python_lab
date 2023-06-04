"""
This module provides classes for managing pens and calculating their prices.
"""
from abc import ABC, abstractmethod
from decorator import logged, LackPenException


class Pen(ABC):
    @logged(LackPenException, mode="console")
    def calculate_price(self, num_pens):
        if num_pens == 0:
            raise LackPenException("Not enough pens")

    def do_something(self):
        """
        Abstract method to perform some action with the pen.

        Subclasses must override this method.
        """

    def __init__(self, num_pencils=None, num_pens=None, num_erasers=None):
        """
        Initializes a pen with the specified quantities of pencils, pens, and erasers.

        :param num_pencils: Number of pencils.
        :param num_pens: Number of pens.
        :param num_erasers: Number of erasers.
        """

        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers

    @abstractmethod
    def calculate_price(self):
        """
        Abstract method to calculate the price of the pen.

        :return: The calculated price.
        """

    def __str__(self):
        """
        Returns a string representation of the pen.

        :return: String representation of the pen.
        """
        return f"Number of Pencils: {self.num_pencils}\nNumber of Pens: {self.num_pens}\n" \
               f"Number of Erasers:" \
               f" {self.num_erasers}"
