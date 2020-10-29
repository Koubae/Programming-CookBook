from itertools import cycle, islice
from collections import namedtuple


Card = namedtuple('Card', 'rank suit')
g = cycle(('red', 'green', 'blue'))
print(list(islice(g, 8)))


def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)

hands = [list() for _ in range(4)]
print(hands)

# ['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green']
# [[], [], [], []]

index = 0
for card in card_deck(): # Print the Whole Dec.
    index = index % 4
    print(index)
    hands[index].append(card)
    index += 1


print('==='*15)
for i in range(5):
    print(i%4)

# 0
# 1
# 2
# 3
# 0
# Cycle Methods
hands = [list() for _ in range(4)]


hands_cycle = cycle(hands)
for card in card_deck():
    next(hands_cycle).append(card)

