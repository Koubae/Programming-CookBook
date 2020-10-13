from collections import namedtuple


Point2D = namedtuple('Point2D', ('x', 'y'))
pt1 = Point2D(10, 20)

Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])
circle_1 = Circle(0, 0, 10)


Stock = namedtuple('Stock', '''symbol
                               year month day
                               open high low close''')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(pt1.x)
print(circle_1.radius)

for item in djia:
    print(item)

x, y = pt1
print(x, y)

symbol, *_, close = djia

print(symbol, close)
print(_)
# >>> DJIA 26393
# >>> [2018, 1, 25, 26313, 26458, 26260]