import numbers


class Point:
    def __init__(self, x: numbers.Real, y: numbers.Real) -> tuple:
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else:
            raise TypeError('Point co-ordinates must be real numbers.')

    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'

    def __len__(self):
        return len(self._pt)

    def __getitem__(self, idx):
        return self._pt[idx]


point_1 = Point(1, 2)
point_2 = Point(3, 5)

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __str__(self):
        return f'These Polygon is made of these points{self._pts} '

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __setitem__(self, s, value):
        try:
            rhs = [Point(*pt) for pt in value]
            is_single = False
        except TypeError:
            try:
                rhs = Point(*value)
                is_single = True
            except TypeError:
                raise TypeError('Invalid Point or Iterable of Points')
        if isinstance(s, int) and is_single or \
                isinstance(s, slice) and not is_single:
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible index/slice assignment')

    def __add__(self, pt): # Is __iadd__ not implemented will use the Super
        if isinstance(pt, Polygon):
            new_pts = self._pts + pt._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with another Polygon')

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts = self._pts + pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts = self._pts + points

    def __iadd__(self, pts):
        self.extend(pts)
        return self

    def append(self, pt):
        self._pts.append(Point(*pt))

    def insert(self, i, pt):
        self._pts.insert(i, Point(*pt))

    def __delitem__(self, s):
        return self._pts[s]

    def pop(self, idx):
        return self._pts.pop(idx)


my_poly = Polygon()
print(my_poly)
my_poly = Polygon(point_1, point_2)
print(my_poly)
print(repr(my_poly))
print(len(my_poly)) # => 2
print(my_poly[1]) # => Point(x=3, y=5)
print(my_poly[0]) # => Point(x=1, y=2)
my_poly[0] = 1,2
print(repr(my_poly))
other_poly = Polygon(range(2), range(2))
print(repr(other_poly))
print(my_poly + other_poly)
print(repr(my_poly))
print(repr(other_poly))
new_poly = my_poly + other_poly
print(repr(new_poly))
new_poly += new_poly
print(repr(new_poly))
new_range = zip(range(3), range(3))
new_point = [Point(*p) for p in new_range]
print(*new_point)
print('---'*5)
my_poly.extend(new_point)
print(repr(my_poly))
print('---'*5)
my_poly = Polygon(*zip(range(3+1), range(3+1)))
print(repr(my_poly))
print('---'*5)
my_poly.append(list(range(2)))
print(repr(my_poly))
print('---'*5)