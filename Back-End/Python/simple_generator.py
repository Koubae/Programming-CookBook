def counter(value:int) -> int: 
    while True:
        value += 1
        yield value

c = counter(0)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
