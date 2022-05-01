from collections import defaultdict
from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps

d = {}



d['a']

result = d.get('a')
type(result)


d.get('a', 0)

counts = {}
sentence = "able was I ere I saw elba"

for c in sentence:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1


# counts

# {'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}


counts = {}
for c in sentence:
    counts[c] = counts.get(c, 0) + 1


#counts


#{'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}

counts = defaultdict(lambda: 0)

for c in sentence:
    counts[c] += 1

#counts


print(isinstance(counts, defaultdict))


#True

print(isinstance(counts, dict))


#True


print(counts.items())


#dict_items([('a', 4), ('b', 2), ('l', 2), ('e', 4), (' ', 6), ('w', 2), ('s', 2), ('I', 2), ('r', 1)])


print(counts['a']) # 4
#counts['python']


persons = {
    'john': {'age': 20, 'eye_color': 'blue'},
    'jack': {'age': 25, 'eye_color': 'brown'},
    'jill': {'age': 22, 'eye_color': 'blue'},
    'eric': {'age': 35},
    'michael': {'age': 27}
}


eye_colors = {}
for person, details in persons.items():
    if 'eye_color' in details:
        color = details['eye_color']
    else:
        color = 'unknown'
    if color in eye_colors:
        eye_colors[color].append(person)
    else:
        eye_colors[color] = [person]


eye_colors = {}
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    person_list = eye_colors.get(color, [])
    person_list.append(person)
    eye_colors[color] = person_list




eye_colors = defaultdict(list)
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    eye_colors[color].append(person)



defaultdict(list,
            {'blue': ['john', 'jill'],
             'brown': ['jack'],
             'Unknown': ['eric', 'michael']})


d = defaultdict(bool, k1=True, k2=False, k3='python')

print(defaultdict(bool, {'k1': True, 'k2': False, 'k3': 'python'}))


persons = {
    'john': defaultdict(lambda: 'unknown',
                        age=20, eye_color='blue'),
    'jack': defaultdict(lambda: 'unknown',
                        age=20, eye_color='brown'),
    'jill': defaultdict(lambda: 'unknown',
                        age=22, eye_color='blue'),
    'eric': defaultdict(lambda: 'unknown', age=35),
    'michael': defaultdict(lambda: 'unknown', age=27)
}


eye_colors = defaultdict(list)
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)



defaultdict(list,
            {'blue': ['john', 'jill'],
             'brown': ['jack'],
             'unknown': ['eric', 'michael']})



eyedict = lambda *args, **kwargs: defaultdict(lambda: 'unknown', *args, **kwargs)


persons = {
    'john': eyedict(age=20, eye_color='blue'),
    'jack': eyedict(age=20, eye_color='brown'),
    'jill': eyedict(age=22, eye_color='blue'),
    'eric': eyedict(age=35),
    'michael': eyedict(age=27)
}



eye_colors = defaultdict(list)
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)


print(eye_colors)

# defaultdict(list,
#             {'blue': ['john', 'jill'],
#              'brown': ['jack'],
#              'unknown': ['eric', 'michael']})



def function_stats():
    d = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)

        return wrapper

    return Stats(decorator, d)

stats = function_stats()
dict(stats.data) # {}


@stats.decorator
def func_1():
    pass


@stats.decorator
def func_2(x, y):
    pass



