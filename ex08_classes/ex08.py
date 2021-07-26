class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
    def rot(self, days, temp):
        self.mold = days * temp

class Rectangle():
    def __init__ (self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len
    def change_size(self, w, l):
        self.width = w
        self.len = l

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(a_hexagon.calculate_perimeter())

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

or1 = Orange(10, "Dark orange")
print(or1)
print(or1.weight)
print(or1.color)
or1.weight = 100
or1.color = "Light orange"
print(or1.weight)
print(or1.color)
or2 = Orange(12, "Yellow orange")
print(or2.mold)
or2.rot(10,33)
print(or2.mold)
