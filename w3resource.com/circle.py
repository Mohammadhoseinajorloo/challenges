import math

class Circle:

    def __init__(self, rediuse):
        self.rediuse = rediuse

    # calculate area 
    def calculate_area(self):
        '''
        a = pi number * 2 pow radiuse 
        '''
        return math.pi * math.pow(self.rediuse, 2)

    # calculate primeter
    def calculate_primeter(self):
        '''
        c = 2 * pi number * rediuse 
        '''
        return 2 * math.pi * self.rediuse

if __name__ == '__main__':
    rediuse = float(input("please enter rediuse: "))
    circle = Circle(rediuse)
    print('area : ', circle.calculate_area())
    print('primeter : ', circle.calculate_primeter())
