from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')
Point2D.__doc__ = 'Represents a 2D Cartesian coordinate'
Point2D.x.__doc__ = 'x-coordinate'
Point2D.y.__doc__ = 'y-coordinate'

print(help(help(Point2D)))