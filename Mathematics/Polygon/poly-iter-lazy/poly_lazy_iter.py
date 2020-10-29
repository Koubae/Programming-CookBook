from math import (sin, cos, tan, pi)


SIDES = {
    3: 'Triangle',
    4: 'Square',
    5: 'Pentagon',
    6: 'Hexagon',
    7: 'Heptagon',
    8: 'Octagon',
    9: 'Nonagon',
    10: 'Decagon'
}


class Polygon:
    def __init__(self, n:int, R:float):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self.__name__ = self.get_type()
        self.name = self.__name__
        self.mapped_polygon = dict()
        self.process_polygon()

    def process_polygon(self): # Pre calculates all the Polygon Properties # Note 1 bottom
        return list([map(lambda x: x, [self.edge_length,
                                       self.interior_angle,
                                       self.apothem,
                                       self.area,
                                       self.perimeter])])

    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'

    def __str__(self):
        return f'{self.name} has got {self._n} Sides, Circumradius={self._R}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._n == other._n and
                    self._R == other._R)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self._n > other._n
        else:
            return NotImplemented

    # Polygon Properties Alias
    @property
    def vertices(self):
        return self._n

    @property
    def edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    # Function Properties
    def polygon_mapper(self, key, value): # Polygon Mapper
        return self.mapped_polygon.setdefault(key, value)

    @property
    def edge_length(self):
        if not self.mapped_polygon.get('edge_length'):
            get_edge_length = (self._R*2) * (sin(pi/self._n))
            return self.polygon_mapper('edge_length', get_edge_length)
        else:
            return self.mapped_polygon.get('edge_length')

    @property
    def interior_angle(self):
        try:
            return self.mapped_polygon['interior_angle']
        except KeyError:
            get_interior_angle = (self._n - 2) * (180 / self._n)
            return self.polygon_mapper('interior_angle', get_interior_angle)

    @property
    def apothem(self):
        try:
            return self.mapped_polygon['apothem']
        except KeyError:
            get_apothem = self._R * (cos(pi/self._n))
            return self.polygon_mapper('apothem', get_apothem)

    @property
    def area(self):
        try:
            return self.mapped_polygon['area']
        except KeyError:
            get_area = (self._n/2) * (self.edge_length * self.apothem)
            return self.polygon_mapper('area', get_area)

    @property
    def perimeter(self):
        try:
            return self.mapped_polygon['perimeter']
        except KeyError:
            get_perimeter = self._n * self.edge_length
            return self.polygon_mapper('perimeter', get_perimeter)

    def get_type(self):
        if self._n in SIDES:
            return SIDES[self._n]


class Polygons: # Iterable, lazy loading
    def __init__(self, max_sides, R):
        if max_sides < 0:
            raise ValueError
        self.max_sides = max_sides
        self.R = R
        self._area_ratio = tuple()

    def __repr__(self):
        return f'Polygons(max_sides={self.max_sides} , R={self.R})'

    def __str__(self):
        return f'Polygons Iterable Max Sides => {self.max_sides}, Common Circumradius {self.R}'

    def __iter__(self):
        return self.PolyIter((self.max_sides, self.R))

    def __contains__(self, polygon):
        return any((polygon.lower() in poly.name.lower())
                   for poly in
                   self)

    @property
    def area_ratio(self):
        if self._area_ratio:
            return self._area_ratio
        else:
            self._area_ratio = max(self.get_poly_ratio())
            return self.area_ratio

    def get_area(self):
        return [poly.area for poly in self]

    def get_perimeter(self):
        return [poly.perimeter for poly in self]

    def get_poly_ratio(self):
        return [(poly[0] / poly[1])
                for poly in
                list(zip(self.get_area(), self.get_perimeter()))]

    class PolyIter: # Iterator, lazy loading
        def __init__(self, polygons):
            self.max_sides = polygons[0]
            self.index = 3
            self.R = polygons[1]

        def __iter__(self):
            return self

        def __next__(self):

            if self.index >= self.max_sides:
                raise StopIteration
            else:
                get_polygons = Polygon(self.index, self.R)
                self.index += 1
                return get_polygons





my_poly = Polygon(3, 1)
set_poly = Polygons(10, 5)
# poly_iter = iter(set_poly)
# print(next(poly_iter))
# print(next(poly_iter))
# print(next(poly_iter))
# print(set_poly.area_ratio)
print(my_poly.interior_angle)
# Note 1, pre calculates all the properties in order to avoid some collisions to when the
# area is called before Edge_length
