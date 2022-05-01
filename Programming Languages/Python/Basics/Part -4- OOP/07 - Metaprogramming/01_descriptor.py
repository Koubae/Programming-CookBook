class IntegerField:
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Must be an integer.')
        instance.__dict__[self.name] = value


class Point:
    x = IntegerField()
    y = IntegerField()
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(10, 20)
p.x, p.y
# (10, 20)

try:
    p.x = 10.5
except TypeError as ex:
    print(ex)
# Must be an integer.