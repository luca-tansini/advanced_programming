from . import shape
import math

Triangle = shape.defineshape("Triangle", lambda side: math.sqrt(3)/4*side**2, lambda side: side*3)
