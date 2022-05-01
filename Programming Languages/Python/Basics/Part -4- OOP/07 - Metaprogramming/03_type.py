
import math

class CustomType(type):
    def __new__(cls, name, bases, class_dict):
        # above is the signature that type.__new__ has - 
        # and args are collected and passed by Python when we call a class (to create an instance of that class)
        # we'll see where those actually come from later
        print('Customized type creation!')
        cls_obj = super().__new__(cls, name, bases, class_dict)  # delegate to super (type in this case)
        cls_obj.circ = lambda self: 2 * math.pi * self.r  # basically attaching a function to the class
        return cls_obj


class_body = """
def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

def area(self):
    return math.pi * self.r ** 2
"""

class_dict = {}
exec(class_body, globals(), class_dict)

Circle = CustomType('Circle', (), class_dict)
# Customized type creation!

type(Circle)
# __main__.CustomType

isinstance(Circle, CustomType), issubclass(CustomType, type)
# (True, True)

hasattr(Circle, '__init__'), hasattr(Circle, 'area')
# (True, True)

c = Circle(0, 0, 1)
c.area()
# 3.141592653589793

hasattr(Circle, 'circ')
# True
c.circ()
# 6.283185307179586