import itertools

from collections import namedtuple

def matrix(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            yield f'{i} x {j} = {i * j}'



list(itertools.islice(matrix(10), 10, 20))


l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']
for x in l1:
    for y in l2:
        print((x, y), end=' ')
    print('')


list(itertools.product(l1, l2))


def matrix(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            yield (i, j, i * j)



list(matrix(4))


def matrix(n):
    for i, j in itertools.product(range(1, n + 1), range(1, n + 1)):
        yield (i, j, i * j)



list(matrix(4))


def matrix(n):
    return ((i, j, i * j)
            for i, j in itertools.product(range(1, n + 1), range(1, n + 1)))



list(matrix(4))


def matrix(n):
    return ((i, j, i * j)
            for i, j in itertools.product(*itertools.tee(range(1, n + 1), 2)))




list(matrix(4))



def grid(min_val, max_val, step, *, num_dimensions=2):
    axis = itertools.takewhile(lambda x: x <= max_val,
                               itertools.count(min_val, step))

    # to handle multiple dimensions, we just need to repeat the axis that
    # many times - tee is perfect for that
    axes = itertools.tee(axis, num_dimensions)

    # and now we just need the product of all these iterables
    return itertools.product(*axes)



list(grid(-1, 1, 0.5))


list(grid(-1, 1, 0.5, num_dimensions=3))


sample_space = list(itertools.product(range(1, 7), range(1, 7)))
print(sample_space)

outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))
print(outcomes)



from fractions import Fraction

odds = Fraction(len(outcomes), len(sample_space))
print(odds)

list(itertools.permutations(l1))


list(itertools.permutations(l1, 2))



list(itertools.permutations('aaa'))


list(itertools.permutations('aba', 2))


list(itertools.combinations([1, 2, 3, 4], 2))


list(itertools.combinations_with_replacement([1, 2, 3, 4], 2))

SUITS = 'SHDC'
RANKS = tuple(map(str, range(2, 11))) + tuple('JQKA')



deck = [rank + suit for suit in SUITS for rank in RANKS]




Card = namedtuple('Card', 'rank suit')



deck = [Card(rank, suit) for suit, rank in itertools.product(SUITS, RANKS)]


sample_space = itertools.combinations(deck, 4)
total = 0
acceptable = 0
for outcome in sample_space:
    total += 1
    for card in outcome:
        if card.rank != 'A':
            break
    else:
        # else block is executed if loop terminated without a break
        acceptable += 1
print(f'total={total}, acceptable={acceptable}')
print('odds={}'.format(Fraction(acceptable, total)))
print('odds={:.10f}'.format(acceptable / total))

total = 270725
acceptable = 1
odds = 1 / 270725
odds = 0.0000036938


all(['A', 'A', '10', 'J'])
l1 = ['K', 'A', 'A', 'A']
l2 = ['A', 'A', 'A', 'A']

print(list(map(lambda x: x == 'A', l1)))
print(list(map(lambda x: x == 'A', l2)))

# [False, True, True, True]
# [True, True, True, True]



print(all(map(lambda x: x == 'A', l1)))
print(all(map(lambda x: x == 'A', l2)))


deck = (Card(rank, suit) for suit, rank in itertools.product(SUITS, RANKS))
sample_space = itertools.combinations(deck, 4)
total = 0
acceptable = 0
for outcome in sample_space:
    total += 1
if all(map(lambda x: x.rank == 'A', outcome)):
    acceptable += 1

print(f'total={total}, acceptable={acceptable}')
print('odds={}'.format(Fraction(acceptable, total)))
print('odds={:.10f}'.format(acceptable / total))

