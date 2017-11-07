import math

class EquilateralTriangle:
    def __init__(self,edge):
        self.__edge = edge

    def calculate_perimeter(self):
        return self.__edge*3

    def calculate_area(self):
        p = self.calculate_perimeter()/2
        return math.sqrt(p*(p-self.__edge)**3)

class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def calculate_perimeter(self):
        return 2*math.pi*self.__radius

    def calculate_area(self):
        return math.pi*self.__radius**2

class Rectangle:
    def __init__(self,edgeA,edgeB):
        self.__edgeA,self.__edgeB = edgeA,edgeB

    def calculate_perimeter(self):
        return 2*(self.__edgeA+self.__edgeB)

    def calculate_area(self):
        return self.__edgeA*self.__edgeB

class Square(Rectangle):
    def __init__(self,edge):
        super(Square,self).__init__(edge,edge)

class Pentagon:
    def __init__(self,edge):
        self.__edge = edge

    def calculate_perimeter(self):
        return self.__edge*5

    def apothem(self):
        return self.__edge * 0.688

    def calculate_area(self):
        return self.calculate_perimeter()*self.apothem()/2

class Hexagon:
    def __init__(self,edge):
        self.__edge = edge

    def calculate_perimeter(self):
        return self.__edge*6

    def apothem(self):
        return self.__edge * 0.866

    def calculate_area(self):
        return self.calculate_perimeter()*self.apothem()/2

shapes = [EquilateralTriangle(2),Circle(2),Rectangle(2,3),Square(2),Pentagon(2),Hexagon(2)]
print("Sorted by perimeter:")
print([(s,s.calculate_perimeter()) for s in sorted(shapes,key=lambda x: x.calculate_perimeter())])
print("Sorted by area:")
print([(s,s.calculate_area()) for s in sorted(shapes,key=lambda x: x.calculate_perimeter())])

class ShapesIterator:
    def __init__(self,list):
        self.__shapes = sorted(list,key=lambda x: x.calculate_area())
        self.__index=0

    def __iter__(self):
        self.__index=0
        return self

    def __next__(self):
        if(self.__index >= len(self.__shapes)): raise StopIteration
        out = self.__shapes[self.__index]
        self.__index+=1
        return out
