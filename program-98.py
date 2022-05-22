# Calculating the area of triangle in OOP (using class and method).


class triangle :                                         # creating the class

    def __init__(self, base , height) :                  # input / constructor method
        self.base = base
        self.height = height

    def calc_area (self) :                               # output method
        area = 0.5 * self.base * self.height
        print('Area of the triangle : ', area)

triangle_1 = triangle (60 , 80)                          # triangle-1
triangle_1.calc_area()

triangle_2 = triangle (30, 40)                           # triangle-2
triangle_2.calc_area()


