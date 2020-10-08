l = [5, 8, 6, 10, 9]

# Calculate max
_max = lambda a, b: a if a > b else b

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(max_sequence(l))
# >>> 10

# Calculate min

_min = lambda a, b: a if a < b else b

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result
print(min_sequence(l))
# >>> 5

# Create a reduce function
def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result
# max
print(_reduce(_max, l))
# min
print(_reduce(_min, l))

# Only lambda
print(_reduce(lambda a, b: a if a > b else b, l))
print(_reduce(lambda a, b: a if a < b else b, l))


