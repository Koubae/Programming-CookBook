from random import randint, random
from collections import namedtuple

Color = namedtuple('Color', 'red green blue alpha')

def random_color():

    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)

color = random_color()

print(color.red)