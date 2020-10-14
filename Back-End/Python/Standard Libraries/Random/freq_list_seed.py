import random
from collections import Counter


def freq_analysis(lst):
    return {k: lst.count(k) for k in set(lst)}

random.seed(0)
lst = [random.randint(0, 10) for _ in range(100)]

query = freq_analysis(lst)
print(query)


random.seed(0)
query_2 = Counter([random.randint(0, 10) for _ in range(100)])
print(query_2)

# query = {0: 5, 1: 13, 2: 7, 3: 9, 4: 11, 5: 9, 6: 6, 7: 10, 8: 13, 9: 11, 10: 6}

# query_2 = Counter({8: 13, 1: 13, 4: 11, 9: 11, 7: 10, 5: 9, 3: 9, 2: 7, 6: 6, 10: 6, 0: 5})