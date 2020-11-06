from collections import defaultdict, Counter
import random
import re

sentence = 'the quick brown fox jumps over the lazy dog'

counter = defaultdict(int)
for c in sentence:
    counter[c] += 1

random.seed(0)
my_list = [random.randint(0, 10) for _ in range(1_000)]
c2 = Counter(my_list)
print(c2)


sentence = '''
his module implements pseudo-random number generators for various distributions.

For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.

On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.

Almost all module functions depend on the 
basic function random(), which generates a 
random float uniformly in the semi-open range 
[0.0, 1.0). Python uses the Mersenne Twister as the core generator. 
It produces 53-bit precision floats and has a period of 2**19937-1. 
The underlying implementation in C is both fast and threadsafe. 
The Mersenne Twister is one of the most extensively tested random number generators in 
existence. However, being completely deterministic, it is not suitable for all purposes,
 and is completely unsuitable for cryptographic purposes.'''

words = re.split('\W', sentence)
word_count = Counter(words)
print(word_count)


c1 = Counter('abba')
for c in c1:
    print(c)

for c in c1.elements():
    print(c)


l = []
for i in range(1, 11):
    for _ in range(i):
        l.append(i)
print(l)

c1 = Counter()
for i in range(1, 11):
    c1[i] = i

print(c1)
#Counter({1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10})


class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]

r = RepeatIterable(x=10, y=20)
print(r.d)


class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]

    def elements(self):
        for k, frequency in self.d.items():
            for i in range(frequency):
                yield k



r = RepeatIterable(a=2, b=3, c=1)

for e in r.elements():
    print(e, end=', ')

#a, a, b, b, b, c,


c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)

c1.update(c2)
print(c1)
# Counter({'c': 5, 'b': 3, 'd': 3, 'a': 1})

c1 = Counter('aabbccddee')
print(c1)
c1.update('abcdef')
print(c1)
# Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2})
# Counter({'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 1})


