class SchoolPen:
    def __init__(self, brand=None, color=None, material=None, size=None, num_pencils=None, num_pens=None,
                 num_erasers=None):
        self.id = "isn-101"
        self.brand = brand
        self.color = color
        self.material = material
        self.size = size
        self.numPencils = num_pencils
        self.numPens = num_pens
        self.numErasers = num_erasers

    def get_id(self):
        return self.id

    def get_brand(self):
        return self.brand

    def get_color(self):
        return self.color

    def get_material(self):
        return self.material

    def get_size(self):
        return self.size

    def set_id(self, id):
        self.id = id

    def set_brand(self, brand):
        self.brand = brand

    def set_color(self, color):
        self.color = color

    def set_material(self, material):
        self.material = material

    def set_size(self, size):
        self.size = size

    def add_pencil(self):
        self.numPencils += 1

    def add_pen(self):
        self.numPens += 1

    def remove_pencil(self):
        if self.numPencils > 0:
            self.numPencils -= 1

    def remove_pen(self):
        if self.numPens > 0:
            self.numPens -= 1

    def __str__(self):
        return "School Pen ID: " + self.id


schoolPens = [SchoolPen(), SchoolPen("Bic", "Blue", "Plastic", 10.0, 2, 1, 1), SchoolPen(),
              SchoolPen("isn-102", "Bic", "Blue", "Plastic", 5.5, 2, 1)]

for schoolPen in schoolPens:
    print(str(schoolPen))
