# Abstract method : the method which has no statements to execute is called an abstract method

# Abstract class : the class under which there is an abstract method

# There is no chance to create 'objects' for an abstract class directly

# The main purpose of an abstract class is to create a 'model class' that would be used by other hierarchical classes after customization

# Calculating the area of triangle and rectangle under an abstract class


from  abc import ABC, abstractmethod                       # importing 'abc' module to implement 'ABC'-abstract base class

class shape (ABC):                                         # creating abstract base class
    def __init__(self, dim1, dim2) :
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area (self) :                                      # abstract method
        pass

class triangle (shape) :
    def area (self) :
        area = 0.5 * self.dim1 * self.dim2
        print('Area of Triangle : ', area)

class rectangle (shape) :
    def area (self) :
        area = self.dim1 * self.dim2
        print('Area of Rectangle : ', area)


t1 = triangle(20, 30)

t1.area()                                                  # Calling the area method of triangle


r1 = rectangle(20, 30)

r1.area()




# We can prove the formation of 'abstract method' in the 'shape' class by creating object for 'shape' class

sh = shape (40, 60)

sh.area()

# It will give the output as error
