from collections import namedtuple


Vector = namedtuple('Vector', 'x1 y1 x2 y2 origin_x origin_y')
#  prototype of a vector with zero origin.
vector_zeroorigin = Vector(x1=None, y1=None, x2=None, y2=None, origin_x=0, origin_y=0)
print(vector_zeroorigin)
# >>> Vector(x1=None, y1=None, x2=None, y2=None, origin_x=0, origin_y=0)


v1 = vector_zeroorigin._replace(x1=1, y1=1, x2=10, y2=10)
print(v1)
# >>> Vector(x1=1, y1=1, x2=10, y2=10, origin_x=0, origin_y=0)