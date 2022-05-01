from collections import namedtuple

Vector = namedtuple('Vector', 'x1 y1 x2 y2 origin_x origin_y')

# setting default values for the last two elements only, i.e. origin_x and origin_y.
Vector.__new__.__defaults__ = (0, 0)
v1 = Vector(0, 0, 10, 10, -10, -10)
print(v1)
# Vector(x1=0, y1=0, x2=10, y2=10, origin_x=-10, origin_y=-10)
v2 = Vector(5, 5, 20, 20)
print(v2)
# Vector(x1=5, y1=5, x2=20, y2=20, origin_x=0, origin_y=0)
v3 = Vector(x1=1, y1=1, x2=10, y2=10)
print(v3)
# Vector(x1=1, y1=1, x2=10, y2=10, origin_x=0, origin_y=0)

# Variant
Vector.__new__.__defaults__ = (0,) * len(Vector._fields)
v5 = Vector()
print(v5)
# Vector(x1=0, y1=0, x2=0, y2=0, origin_x=0, origin_y=0)