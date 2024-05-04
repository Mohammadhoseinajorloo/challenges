import math

class Represents_Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def __repr__(self):
        text = ''
        text += f"area: {self.calculate_area()}\n"
        text += f"perimeter: {self.calculate_perimeter()}\n "
        return text

class Circle(Represents_Shape):

    def __init__(self, radiuse):
        self.radiuse = radiuse 

    def calculate_area(self):
        return math.pi * math.pow(self.radiuse, 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radiuse 


class Tringle(Represents_Shape):


    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square(Represents_Shape):


    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__': 
    calculate = input('please choose shape calculate:\n1.cricle\n2.Triangle\n3.square\n?:')
    if calculate == '1': 
        radiuse = float(input('please enter radiuse: '))
        circle = Circle(radiuse)
    elif calculate == "2":
        base = float(input('please enter base: '))
        height = float(input('please enter height: '))
        side1 = float(input('please enter side1: '))
        side2 = float(input('please enter side2: '))
        side3 = float(input('please enter side3: '))
        triangle = Tringle(base, height, side1, side2, side3)
    elif calculate == '3': 
        length = float(input('please enter lenghth: '))
        width = float(input('please enter width: '))
        square = Square(length, width)
