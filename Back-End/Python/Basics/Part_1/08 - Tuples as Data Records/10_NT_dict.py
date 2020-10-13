from collections import namedtuple


# Dict
data_dict = dict(key1=100, key2=200, key3=300)
Data = namedtuple('Data', data_dict.keys())
print(Data._fields) # ('key1', 'key2', 'key3')

# Create Namedtuple with Sorted
data_dict = dict(first_name='John', last_name='Cleese', age=42, complaint='dead parrot')

Struct = namedtuple('Struct', sorted(data_dict.keys()))
print(Struct._fields) # ('age', 'complaint', 'first_name', 'last_name')
d1 = Struct(**data_dict)
print(d1) # Struct(age=42, complaint='dead parrot', first_name='John', last_name='Cleese')

# Now has same methods as a Dict
key_name = 'age'
getattr(d1, key_name)
print(data_dict.get('age', None), data_dict.get('invalid_key', None))
print(getattr(d1, 'age', None), getattr(d1, 'invalid_field', None))


data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)

keys = {key for dict_ in data_list for key in dict_.keys()}
print(keys) # {'key3', 'key1', 'key2'}

keys = set().union(*(dict_.keys() for dict_ in data_list))
print(keys)
Struct = namedtuple('Struct', keys)
print(Struct._fields) # ('key1', 'key2', 'key3')

# set the default to None if the key is missing
Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
#  load up all these dictionaries into a new list of named tuples
tuple_list = [Struct(**dict_) for dict_ in data_list]
print(tuple_list)
# [Struct(key3=None, key1=1, key2=2), Struct(key3=None, key1=3, key2=4),
# Struct(key3=7, key1=5, key2=6), Struct(key3=None, key1=None, key2=100)]


# Packaged in a simple function
def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('struct', keys)
    Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

print(tuplify_dicts(data_list))
# [Struct(key2=2, key1=1, key3=None), Struct(key2=4, key1=3, key3=None), Struct(key2=6, key1=5, key3=7), Struct(key2=100, key1=None, key3=None)]
# [struct(key2=2, key1=1, key3=None), struct(key2=4, key1=3, key3=None), struct(key2=6, key1=5, key3=7), struct(key2=100, key1=None, key3=None)]