"""
This module provides classes for managing pens and calculating their prices.
"""
from models.school_pen import SchoolPen
from models.marker_pen import MarkerPen


class PenManager:
    """
    Class representing a pen manager.
    """
    def __init__(self):
        """
        Initializes a pen manager with an empty pen list.
        """
        self.pen_list = []

    def add_pen(self, pen):
        """
        Adds a pen to the pen manager.

        :param pen: The pen to add.
        """
        self.pen_list.append(pen)

    def display_pens(self):
        """
        Displays the information about the pens in the pen manager.
        """
        for pen in self.pen_list:
            print(pen)
            print("Price:", pen.calculate_price())
            print()


schoolPen1 = SchoolPen(num_pencils=2, num_pens=1, num_erasers=1)
schoolPen2 = SchoolPen(num_pencils=5, num_pens=2, num_erasers=1)
markerPen = MarkerPen(num_pens=3)

manager = PenManager()
manager.add_pen(schoolPen1)
manager.add_pen(schoolPen2)
manager.add_pen(markerPen)

manager.display_pens()
