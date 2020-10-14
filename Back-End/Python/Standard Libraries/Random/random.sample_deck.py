from collections import Counter
import random

# population sample ,once an element has been randomly selected, it cannot be selected again instead of random.choices where the population of the obj becomes infinite.


suits = 'C', 'D', 'H', 'A'
ranks = tuple(range(2,11)) + tuple('JQKA')

deck = [str(rank) + suit
        for suit in suits
        for rank in ranks]
print(deck)

result = Counter(random.sample(deck, k=20))
print(result)