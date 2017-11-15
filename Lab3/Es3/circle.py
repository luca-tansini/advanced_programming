from . import shape
import math

Circle = shape.defineshape("Circle", lambda radius: math.pi*radius**2, lambda radius: 2*math.pi*radius)
