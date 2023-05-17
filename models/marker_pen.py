from models.school_pen import pen


class marker_pen(pen):
    PRICE_PER_MARKER = 3.0

    def calculate_price(self):
        return self.num_pens * self.PRICE_PER_MARKER
