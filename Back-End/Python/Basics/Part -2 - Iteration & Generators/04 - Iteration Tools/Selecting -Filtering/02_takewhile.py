from itertools import takewhile
from math import sin, pi

# The takewhile function in the itertools module will yield elements from an iterable, as long as a specific criteria (the predicate) is True.
#
# As soon as the predicate is False,
# iteration is stopped - even if subsequent
# elements would have had a True predicate
# - this is not a filter, this basically iterate over an
# iterable as long as the predicate remains True.

def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start) / (n-1)
    for _ in range(n):
        yield round(sin(start), 2)
        start += step

print(list(sine_wave(15)))
# [0.0, 0.43, 0.78, 0.97, 0.97, 0.78, 0.43, 0.0, -0.43, -0.78, -0.97, -0.97, -0.78, -0.43, -0.0]

print(list(takewhile(lambda x: 0 <= x <= 0.9, sine_wave(15))))
# [0.0, 0.43, 0.78]
print(list(filter(lambda x: 0 <= x <= 0.9, sine_wave(15))))
# [0.0, 0.43, 0.78, 0.78, 0.43, 0.0, -0.0]
