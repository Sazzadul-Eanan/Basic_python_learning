# A practical example of inheritance

# Calculating the area of triangle and rectangle

class shape :                                         # A Template class of common properties to override
    def __init__(self, dim1, dim2) :
        self.dim1 = dim1
        self.dim2 = dim2
    def area (self) :
        print ('I am area method of shape class')

class triangle (shape) :
    def area (self) :                                 # Overriding the area method
        area = 0.5 * self.dim1 * self.dim2
        print('Area of Triangle : ', area)

class rectangle (shape) :
    def area (self) :                                 # Overriding the area method
        area = self.dim1 * self.dim2
        print('Area of Rectangle : ', area)


t1 = triangle(20, 30)                                 # Creating triangle object

t1.area()                                             # Calling area method


r1 = rectangle(20, 30)                                # Creating rectangle object

r1.area()