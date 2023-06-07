"""
This module provides classes for managing pens and calculating their prices.

The module includes abstract base classes for pens and concrete subclasses representing
different types of pens.
It also provides a PenManager class for managing a collection of pens and performing various
operations on them.

Classes:
- Pen (ABC): Abstract base class representing a pen.
- SchoolPen (Pen): Concrete subclass representing a school pen.
- MarkerPen (Pen): Concrete subclass representing a marker pen.
- PenManager: Class for managing a collection of pens.

Usage example:
# Create some pen objects
schoolPen1 = SchoolPen(num_pencils=2, num_pens=1, num_erasers=1)
schoolPen2 = SchoolPen(num_pencils=5, num_pens=2, num_erasers=1)
markerPen = MarkerPen(num_pens=3)

# Create a pen manager
manager = PenManager()

# Add pens to the manager
manager.add_pen(schoolPen1)
manager.add_pen(schoolPen2)
manager.add_pen(markerPen)

# Display information about the pens in the manager
manager.display_pens()
"""
from models.school_pen import SchoolPen
from models.marker_pen import MarkerPen
from decorator import logged, LackPenException
from exceptions import LackPenException


class PenManager:
    """
    Class representing a pen manager.
    """

    def __init__(self):
        """
        Initializes a pen manager with an empty pen list.
        """
        self.pen_list = []

    def add_pen(self, _pen):
        """
        Adds a pen to the pen manager.

        :param _pen: The pen  to add.
        """
        self.pen_list.append(_pen)

    def display_pens(self):
        """
        Displays the information about the pens in the pen manager.
        """
        for _pen in self.pen_list:
            print(_pen)
            print("Price:", _pen.calculate_price())
            print()

    class LackPenException(Exception):

        pass

    def __len__(self):
        """
        Returns the number of pens in the pen manager.

        :return: The number of pens.
        """
        return len(self.pen_list)

    def __getitem__(self, _index):
        """
        Returns the pen at the specified index in the pen manager.

        :param _index: The index of the pen.
        :return: The pen at the specified index.
        """
        return self.pen_list[_index]

    def __iter__(self):
        """
        Returns an iterator over the pens in the pen manager.

        :return: An iterator over the pens.
        """
        return iter(self.pen_list)

    def get_results(self):
        """
        Returns a list of results from calling the "do_something()" method on each pen.

        :return: A list of results.
        """
        return [_pen.do_something() for _pen in self.pen_list]

    def get_enumerated_pens(self):
        """
        Returns a concatenation of the pen and its index in the pen manager.

        :return: A concatenation of the pen and its index.
        """
        return [(_index, _pen) for _index, _pen in enumerate(self.pen_list)]

    def get_combined_results(self):
        """
        Returns a concatenation of the pen and the result of the "do_something()" method.

        :return: A concatenation of the pen and the result.
        """
        return [(_pen, _pen.do_something()) for _pen in self.pen_list]

    def get_attributes_by_type(self, data_type):
        """
        Returns a dictionary with attributes and their values for a given data type.

        :param data_type: The data type to filter attributes.
        :return: A dictionary of attributes and values.
        """
        return {key: value for key, value in self.pen_list[0].__dict__.items() if isinstance(value, data_type)}

    def check_conditions(self, condition):
        """
        Checks if all and any objects in the pen manager satisfy a given condition.

        :param condition: The condition to check.
        :return: A dictionary with "all" and "any" keys and boolean values.
        """
        return {
            "all": all(condition(_pen) for _pen in self.pen_list),
            "any": any(condition(_pen) for _pen in self.pen_list)
        }


schoolPen1 = SchoolPen(num_pencils=2, num_pens=0, num_erasers=1)
schoolPen2 = SchoolPen(num_pencils=5, num_pens=2, num_erasers=1)
markerPen = MarkerPen(num_pens=3)

manager = PenManager()

manager.add_pen(schoolPen1)
manager.add_pen(schoolPen2)
manager.add_pen(markerPen)

manager.display_pens()

#raise LackPenException()
