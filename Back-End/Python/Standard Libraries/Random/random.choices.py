import random
from collections import namedtuple
from time import perf_counter

list_1 = list(range(1000))

for _ in range(5):
    print(random.choices(list_1, k=3))
# OUTPUT
# [610, 85, 428]
# [241, 271, 599]
# [230, 687, 504]
# [979, 883, 239]
# [883, 409, 101]

#  we can make the sample size larger than the population:
print('==='*15, end='\n\n')

list_2 = ['a', 'b', 'c']

for _ in range(10):
    print(random.choices(list_2, k=5))

# OUTPUT
# ['a', 'a', 'c', 'a', 'a']
# ['c', 'a', 'b', 'a', 'b']
# ['c', 'a', 'b', 'c', 'b']
# ['b', 'c', 'b', 'a', 'c']
# ['a', 'c', 'c', 'a', 'a']
# ['b', 'a', 'c', 'a', 'b']
# ['c', 'b', 'a', 'a', 'b']
# ['b', 'b', 'c', 'c', 'b']
# ['c', 'b', 'c', 'b', 'b']
# ['a', 'a', 'c', 'a', 'c']
print('==='*15, end='\n\n')

# Specify a weight

weights_2 = [10, 1, 1]

for _ in range(10):
    print(random.choices(list_2, k=5, weights=weights_2))

# OUTPUT
# ['b', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'c']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'c', 'a', 'a', 'a']
# ['a', 'a', 'c', 'b', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'b', 'a', 'a']
print('==='*15, end='\n\n')

weights_2 = [100, 1, 1]

for _ in range(10):
    print(random.choices(list_2, k=5, weights=weights_2))

# OUTPUT
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
# ['a', 'a', 'a', 'a', 'a']
print('==='*15, end='\n\n')


Freq = namedtuple('Freq', 'count freq')

def freq_counts(list_):
    total = len(list_)
    return {k: Freq(list_.count(k), 100 * list_.count(k)/total) for k in set(list_)}

result = freq_counts(random.choices(list_2, k=1000))
print(result)
# {'b': Freq(count=324, freq=32.4), 'c': Freq(count=340, freq=34.0), 'a': Freq(count=336, freq=33.6)}

random.seed(0)
result = freq_counts(random.choices(list_2, k=1_000, weights=(8, 1, 1)))
print(result)



denominators = random.choices([0, 1], k=1_000_000)

start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)* 10_000}')
# Avg elapsed time: 0.000761879

start = perf_counter()
for denominator in denominators:
    try:
        10 / denominator
    except ZeroDivisionError:
        continue

end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)* 10_000}')
# Avg elapsed time: 0.002059605

denominators = random.choices([0, 1], k=1_000_000, weights=[1, 9])
start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)* 10_000}')
# Avg elapsed time: 0.0008426379999999999


start = perf_counter()
for denominator in denominators:
    try:
        10 / denominator
    except ZeroDivisionError:
        continue
        
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)* 10_000}')

# Avg elapsed time: 0.0009672220000000009