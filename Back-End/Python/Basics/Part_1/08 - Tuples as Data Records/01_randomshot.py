from random import uniform
from math import sqrt


def random_shot(radius):
    '''Generates a random 2D coordinate within
    the bounds [-radius, radius] * [-radius, radius]
    (a square of area 4)
    and also determines if it falls within
    a circle centered at the origin
    with specified radius'''

    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False

    return random_x, random_y, is_in_circle


num_attempts = 1_000_000
count_inside = 0
for i in range(num_attempts):
    *_, is_in_circle = random_shot(5)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately: {4 * count_inside / num_attempts}')

# >>> Pi is approximately: 3.141372