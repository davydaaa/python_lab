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

    def addpencil(self):
        self.numPencils += 1

    def addpen(self):
        self.numPens += 1

    def removepencil(self):
        if self.numPencils > 0:
            self.numPencils -= 1

    def removepen(self):
        if self.numPens > 0:
            self.numPens -= 1

    def __str__(self):
        return "School Pen ID: " + self.id


schoolPens = [None] * 4
schoolPens[0] = SchoolPen()
schoolPens[1] = SchoolPen("Bic", "Blue", "Plastic", 10.0, 2, 1, 1)
schoolPens[2] = SchoolPen()
myPen = SchoolPen("isn-102", "Bic", "Blue", "Plastic", 5.5, 2, 1)

for schoolPen in schoolPens:
    print(str(schoolPen))
