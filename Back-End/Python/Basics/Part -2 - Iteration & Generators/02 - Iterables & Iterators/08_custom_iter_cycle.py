import itertools


class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result


# FOR LOOP
n = 10
iter_cycl = CyclicIterator('NSWE')
for i in range(1, n+1):
    direction = next(iter_cycl)
    print(f'{i}{direction}')
# 1N
# 2S
# 3W
# 4E
# 5N
# 6S
# 7W
# 8E
# 9N
# 10S

print('==='*15)
# LIST COMPREHENSION
n = 10
iter_cycl = CyclicIterator('NSWE')
print([f'{i}{next(iter_cycl)}' for i in range(1, n+1)])
# ['1N', '2S', '3W', '4E', '5N', '6S', '7W', '8E', '9N', '10S']

print('==='*15)
n = 10
list(zip(range(1, n+1), 'NSWE' * (n//4 + 1)))

print([f'{i}{direction}'
       for i, direction in zip(range(1, n+1), 'NSWE' * (n//4 + 1))])


print('==='*15)
n = 10
iter_cycl = CyclicIterator('NSWE')
print([f'{i}{next(iter_cycl)}' for i in range(1, n+1)])

print('==='*15)
n = 10
iter_cycl = itertools.cycle('NSWE')
print([f'{i}{next(iter_cycl)}' for i in range(1, n+1)])


# All Entries:
# ['1N', '2S', '3W', '4E', '5N', '6S', '7W', '8E', '9N', '10S']