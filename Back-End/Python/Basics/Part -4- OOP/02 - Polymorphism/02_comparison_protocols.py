from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
        
    def __eq__(self, other):
        print('__eq__ called...')
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __lt__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented
    
    def __le__(self, other):
        return self == other or self < other

v1 = Vector(0, 0)
v2 = Vector(1, 1)
print(v1 != v2)