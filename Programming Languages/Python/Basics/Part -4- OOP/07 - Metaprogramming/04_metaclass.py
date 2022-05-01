import math

class CustomType(type):
    def __new__(mcls, name, bases, class_dict):
        print(f'Using custom metaclass {mcls} to create class {name}...')
        cls_obj = super().__new__(mcls, name, bases, class_dict)
        cls_obj.circ = lambda self: 2 * math.pi * self.r
        return cls_obj


class Circle(metaclass=CustomType):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
        return math.pi * self.r ** 2

#  Using custom metaclass <class '__main__.CustomType'> to create class Circle...

c = Circle(0, 0, 1)
print(c.area())
print(c.circ())