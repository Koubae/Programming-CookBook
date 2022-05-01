class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __hash__(self):
        return hash((self.x, self.y))

points = {Point(0, 0): 'origin', Point(1,1): 'pt at (1,1)'}
print(points[Point(0,0)])
# 'origin'

# OR

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Point(*other)
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __hash__(self):
        return hash((self.x, self.y))

pt = Point(0,0)
print(pt.x) # 0
# pt.x = 10

# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-100-634eaafb5eab> in <module>
# ----> 1 pt.x = 10

# AttributeError: can't set attribute
