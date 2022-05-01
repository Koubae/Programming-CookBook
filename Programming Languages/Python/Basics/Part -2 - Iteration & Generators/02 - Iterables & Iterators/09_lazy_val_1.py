import math


class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None: # Check if area Exists
            print('Calculating area...')
            self._area = math.pi * self.radius ** 2
        return self._area   # Else Returns back area


c = Circle(1)
print(c.area)
# Calculating area...
# 3.141592653589793
print(c.area)

# 3.141592653589793
c.radius = 2
print(c.area)
# Calculating area...
# 12.566370614359172
