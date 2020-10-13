from collections import namedtuple

Point2D = namedtuple('Point2D', ('x', 'y'))
pt1 = Point2D(10, 20)

Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])
circle_1 = Circle(0, 0, 10)


Stock = namedtuple('Stock', '''symbol
                               year month day
                               open high low close''')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

# FIELDS
print(Point2D._fields) # ('x', 'y')
print(Stock._fields)
# ('symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close')


# Converting Named Tuples to Dictionaries
print(pt1._asdict()) # {'x': 10, 'y': 20}

for i in dir(Point2D):
    print(i)

# _asdict
# _field_defaults
# _fields
# _fields_defaults
# _make
# _replace