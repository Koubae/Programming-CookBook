from itertools import groupby
from operator import itemgetter

lst = [1, 1, 3, 5, 1, 4, 4]

res = { k : [i for i, _ in group] for k, group in groupby(sorted(enumerate(lst), key=itemgetter(1)), key=itemgetter(1))}
print(res)
# {1: [0, 1, 4], 3: [2], 4: [5, 6], 5: [3]}
#  O(NlogN)