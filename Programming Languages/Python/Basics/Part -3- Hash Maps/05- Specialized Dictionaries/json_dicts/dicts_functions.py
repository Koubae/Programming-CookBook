from collections import defaultdict, Counter, ChainMap
import json
from pprint import pprint
from random import seed, choices


d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}


counter_1 = defaultdict(int)

x = [[(k, v) for k,v in d] for d in [d1.items(), d2.items(), d3.items()]]
for i in x:
    for k,v in i:
        counter_1[k] += v
#pprint(counter_1, indent=2)

counter_2 = defaultdict(int)
x = ChainMap(d1, d2, d3).maps
for item in x:
    for k, v in item.items():
        counter_2[k] += v
#pprint(counter_2, indent=2)


y = ChainMap(d1, d2, d3).maps
cnt = Counter()
for item in y:
    for k, v in item.items():
        cnt[k] += (0 + v)
#pprint(cnt, indent=2)


def merge(*dicts):
    unsorted = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            unsorted[k] += v
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))

pprint(merge(d1, d2, d3), indent=2)


def merge(*dicts):
    result = Counter()
    for d in dicts:
        result.update(d)

    return dict(result.most_common())

pprint(merge(d1, d2, d3), indent=2)

class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color

    def __repr__(self):
        return f'Person(eye_color={self.eye_color})'


eye_colors = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")
seed(0)
persons = [Person(color) for color in choices(eye_colors[2:], k = 50)]

def count_eye_color(colors, people):
    cnt = Counter()
    for color in colors:
        for p in people:
            if color == p.eye_color:
                cnt[color] += 1
            else:
                cnt[color] += 0
    return cnt

get_result = count_eye_color(eye_colors, persons)
#pprint(get_result, indent=2)



def count_eye_colors(persons, possible_eye_colors):
    counts = Counter({color: 0 for color in possible_eye_colors}) # Create a Counter Object,defaultskey with Valuse 0
    counts.update(p.eye_color for p in persons)
    return counts


pprint(count_eye_colors(persons, eye_colors), indent=2)


def load_settings(env):
    # assume file name is <env>.json
    with open(f'{env}.json') as f:
        settings = json.load(f)
    return settings

def chain_recursive(d1, d2):
    chain = ChainMap(d1, d2)
    for k, v in d1.items():
        if isinstance(v, dict) and k in d2:
            chain[k] = chain_recursive(d1[k], d2[k]) # Recursively Creates Chains for each subDicts
    return chain

def settings(env):
    common_settings = load_settings('common')
    env_settings = load_settings(env)
    return chain_recursive(env_settings, common_settings)


prod = settings('prod')
dev = settings('dev')