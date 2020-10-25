from math import (sin,
                  cos,
                  tan,
                  pi)

FIGURES = {
    'triangle': 3,
    'square': 4,
    'pentagon': 5,
    'hexagon': 6,
    'heptagon': 7,
    'octagon': 8,
    'nonagon': 9,
    'decagon': 10
}

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


# TODO Change Property Functions / Make Alias of the properties
class Polygon:

    def __init__(self, sides: int, circumradius: float):
        if sides >= 3:
            self._sides = sides
            self.__name__ = self.get_type()
        else:
            raise TypeError('Polygon must have at least 3 edges')
        self.circumradius = circumradius
        self.R = circumradius # Circumradius Alias
        self.n = sides # Number of Sides Alias
        self.name = self.__name__


    @property
    def edges(self):
        return self._sides

    @edges.getter
    def edges(self):
        return self._sides

    @edges.setter
    def edges(self, value):
        if isinstance(value, int):
            setattr(self, '_sides' ,value)
        else:
            if isinstance(value, float):
                print('The number of edges must be an Integer value, not a Floating Point value')
                print(self._sides)

    @property
    def vertices(self):
        return self._sides

    @vertices.getter
    def vertices(self):
        return self._sides

    @vertices.setter
    def vertices(self, value):
        if isinstance(value, int) or isinstance(value, float):
            setattr(self, '_sides', value)
        else:
            print('Invalid Input')

    def __repr__(self):
        return f'Polygon(edges={self._sides}, circumradius={self.circumradius})'

    def __eq__(self, other):  # Based on #edges & Circumradius
        if isinstance(other, Polygon):
            if self.edges == other.edges and self.circumradius == other.circumradius:
                return True
            else:
                return False
        else:
            print('Equality evaluation is possible only with 2 Polygons')
            return NotImplemented

    def __gt__(self, other):  # Based on # Vertices
        if isinstance(other, Polygon):
            if self.edges > other.edges:
                return True
            else:
                return False
        else:
            return NotImplemented
    @property
    def interior_angle(self): # Given #edges
        return (self.n-2) * (180/self.n)

    @property
    def edge_length(self): # First, given Circumradius & #Edges
        return (self.R*2) * (sin(pi / self.edges))

    @property # Given the Circumradius and #edges
    def apothem(self):
        return self.R * (cos(pi / self.edges))

    @property
    def area(self): # Given the edge_length, Apother and #sides
        return (self.n / 2) * (self.edge_length * self.apothem)

    @property
    def perimeter(self): # Given the edge_length
        return self.n * self.edge_length

    def get_type(self): # Gets name of Figure
        if self._sides in SIDES:
            return SIDES[self._sides]


class Polygons:
    def __init__(self, max_sides: list, r: float):
        if max_sides > 0:
            self.max_sides = range(3, max_sides+1)
        else:
            raise ValueError
        self.R = r
        self.polygons = [Polygon(side_, self.R) for side_ in self.max_sides]

    @property
    def max_area_per_ratio(self):
        return max(self.get_poly_ratio())

    def __repr__(self):
        return f'Polygons(max_sides={self.max_sides} , R={self.R})'

    def __str__(self):
        return f'These is the Polygons Sequence={self.polygons}'

    def __len__(self):
        return len(self.polygons)

    def __getitem__(self, poly):
        return self.polygons[poly]

    def __contains__(self, polygon):
        return any((polygon.lower() in poly.name.lower())
                   for poly in self.polygons)

    def get_area(self):
        return [poly.area for poly in self.polygons]

    def get_perimeter(self):
        return [poly.perimeter for poly in self.polygons]

    def get_poly_ratio(self):
        return [(poly[0] / poly[1])
                for poly in
                list(zip(self.get_area(), self.get_perimeter()))]






