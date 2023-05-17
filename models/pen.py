from abc import ABC, abstractmethod


class pen(ABC):
    def __init__(self, num_pencils=None, num_pens=None, num_erasers=None):
        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers

    @abstractmethod
    def calculate_price(self):
        pass

    def __str__(self):
        return f"Number of Pencils: {self.num_pencils}\nNumber of Pens: {self.num_pens}\nNumber of Erasers:" \
               f" {self.num_erasers}"
