d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
union = d1.keys() | d2.keys()
intersection = d1.keys() & d2.keys()
keys = union - intersection

result = {}
for key in keys:
    result[key] = d1.get(key) or d2.get(key)
print(result)
# {'e': 5, 'd': 4}

result = {key: d1.get(key) or d2.get(key) for key in keys}
print(result)
# {'e': 5, 'd': 4}

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
result = {key: d1.get(key) or d2.get(key)
        for key in d1.keys() ^ d2.keys()}
print(result)
# {'e': 5, 'd': 4}


result = {}
for d1.keys() ^ d2.keys():
    result[key] = d1.get(key) or d2.get(key)
print(result)
# {'e': 5, 'd': 4}