from models.school_pen import school_pen
from models.marker_pen import marker_pen


class pen_manager:
    def __init__(self):
        self.penList = []

    def add_pen(self, _pen):
        self.penList.append(_pen)

    def display_pens(self):
        for _pen in self.penList:
            print(_pen)
            print("Price:", _pen.calculate_price())
            print()


# Create instances of Pen subclasses
schoolPen1 = school_pen(num_pencils=2, num_pens=1, num_erasers=1)
schoolPen2 = school_pen(num_pencils=5, num_pens=2, num_erasers=1)
markerPen = marker_pen(num_pens=3)

# Create PenManager instance and add pens
manager = pen_manager()
manager.add_pen(schoolPen1)
manager.add_pen(schoolPen2)
manager.add_pen(markerPen)

# Display pens and prices
manager.display_pens()
