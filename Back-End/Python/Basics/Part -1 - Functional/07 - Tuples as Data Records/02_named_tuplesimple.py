from collections import namedtuple

# List
Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])

circle_1 = Circle(0, 0, 0)
circle_2 = Circle(center_x=10, center_y=20, radius=100)

print(circle_1)
print(circle_2)

# String
City = namedtuple('City', 'name country population')
new_york = City('New York', 'USA', 8_500_000)

# Tuple
Stock = namedtuple('Stock', 'symbol, year, month, day, open, high, low, close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

# String with no commas + multiline
Stock = namedtuple('Stock', '''symbol
                               year month day
                               open high low close''')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)