import math
#Closure che genera le classi
#Per i poligoni side è il lato, per  cerchi sarebbe il raggio
def defineshape(name, farea, fperimeter):
    class Shape():
        def __init__(self, side):
            self.side = side
            self.name = name

        #calcolo l'area utilizzando solo il lato
        def calculate_area(self):
            return farea(self.side)

        def calculate_perimeter(self):
            return fperimeter(self.side)

        def true_lt(self,other):
            return self.calculate_area() < other.calculate_area()

        def __lt__(self,other):
            return self.true_lt(other)

        def __str__(self):
            sideorradius = "radius" if name=="Circle" else "side"
            return "{0} with {1}: {2}".format(name,sideorradius,self.side)
    return Shape
