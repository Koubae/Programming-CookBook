class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._area = None
        self._radius = value
        
    @property
    def area(self):
        if self._area is None:
            # value not cached - calculate it
            print('Calculating area...')
            self._area = pi * (self.radius ** 2)
        return self._area


c = Circle(1)
print(c.area)