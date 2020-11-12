import json


json_data = """{
    "Alex": {"age": 18},
    "Bryan": {"age": 21, "city": "London"},
    "Guido": {"age": "unknown"}
}"""

data = json.loads(json_data)
data
# {'Alex': {'age': 18},
#  'Bryan': {'age': 21, 'city': 'London'},
#  'Guido': {'age': 'unknown'}}



class Person:
    __slots__ = 'name', '_age'
    
    def __init__(self, name):
        self.name = name
        self._age = None
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError('Invalid age')
            
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

persons = []
for name, attributes in data.items():
    try:
        p = Person(name)
        
        for attrib_name, attrib_value in attributes.items():
            try:
                setattr(p, attrib_name, attrib_value)
            except AttributeError:
                print(f'ignoring attribute: {name}.{attrib_name}={attrib_value}')
    except ValueError as ex:
        print(f'Data for Person({name}) contains an invalid attribute value: {ex}')
    else:
        # note that this runs if the outer try does not encounter an exception
        # since the inner try catches and does not propagate an `AttributeError`
        # this does not affect this else - the outer try never sees the inner exception
        # since it was handled (and essentially silenced)
        persons.append(p)
        
print(persons)
# ignoring attribute: Bryan.city=London
# Data for Person(Guido) contains an invalid attribute value: Invalid age
# [Person(name=Alex, age=18), Person(name=Bryan, age=21)]
# While we could certainly handle the ValueError in the nested for loop, it makes the logic a bit more difficult:

persons = []
for name, attributes in data.items():
    p = Person(name)

    for attrib_name, attrib_value in attributes.items():
        skip_person = False
        try:
            setattr(p, attrib_name, attrib_value)
        except AttributeError:
            print(f'ignoring attribute: {name}.{attrib_name}={attrib_value}')
        except ValueError as ex:
            print(f'Data for Person({name}) contains an invalid attribute value: {ex}')
            skip_person = True
            break
    if not skip_person:
        persons.append(p)
        
print(persons)


def convert_int(val):
    if not isinstance(val, int):  # remember this will work for booleans too!
        raise TypeError()
    if val not in {0, 1}:
        raise ValueError("Integer values 0 or 1 only")
    return bool(val)
def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()
        
    val = val.casefold()  # for case-insensitive comparisons
    if val in {'0', 'f', 'false'}:
        return False
    elif val in {'1', 't', 'true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False (case insensitive)')

class ConversionError(Exception):
    pass

def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            # it wasn't an int/bool, so let's try it as a string
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'The type {type(val).__name__} cannot be converted to a bool')
    except ValueError as ex:
        # this will catch ValueError exceptions from either convert_int or convert_str
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
    else:
        return b


values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)

    print(value, result)


class ConversionError(Exception):
    pass

def make_bool(val):
    try:
        b = convert_int(val)
    except TypeError:
        pass  # for now we ignore type errors
    except ValueError as ex:
        # it wasn't an int/bool, so let's try it as a string
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
    else:
        return b
    
    # reached here so we must have had a type error
    try:
        b = convert_str(val)
    except TypeError:
        pass  # silence this again
    except ValueError as ex:
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
    else:
        return b
        
    # reached here, so neither an int nor a string
    raise ConversionError(f'The type {type(val).__name__} cannot be converted to a bool')

values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)

    print(value, result)
# 1.0 The type float cannot be converted to a bool


def make_bool(val):
    if isinstance(val, int):
        if val in {0, 1}:
            return bool(val)
        else:
            raise ConversionError('Invalid integer value.')
    if isinstance(val, str):
        if val.casefold() in {'1', 'true', 't'}:
            return True
        if val.casefold() in {'0', 'false', 'f'}:
            return False
        raise ConversionError('Invalid string value')
    raise ConversionError('Invalid type')

values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)

    print(value, result)


def get_item_forgive_me(seq, idx, default=None):
    try:
        return seq[idx]
    except (IndexError, TypeError, KeyError):
        # catch either not indexable (TypeError), or index out of bounds, 
        # or even a KeyError for mapping types
        return default


def get_item_ask_perm(seq, idx, default=None):
    if hasattr(seq, '__getitem__'):
        if idx < len(seq):
            return seq[idx]
    return default



get_item_forgive_me([1, 2, 3], 0)
# 1

get_item_forgive_me([1, 2, 3], 10, 'Nope')
# 'Nope'

get_item_ask_perm([1, 2, 3], 0)
# 1

get_item_ask_perm([1, 2, 3], 10, 'Nope')
# 'Nope'

get_item_forgive_me({'a': 100}, 'a')
# 100
get_item_ask_perm({'a': 1}, 'a')


def get_item_ask_perm(seq, idx, default=None):
    if hasattr(seq, '__getitem__'):
        # could be sequence type or mapping type, or something else altogether??
        if isinstance(seq, dict):
            return seq.get(idx, default)
        elif isinstance(idx, int):
            # looks like a numerical index...
            if idx < len(seq):
                return seq[idx]
    return default


get_item_ask_perm({'a': 100}, 'a')
# 100
get_item_ask_perm([1, 2, 3], 0)
# 1


class ConstantSequence:
    def __init__(self, val):
        self.val = val
        
    def __getitem__(self, idx):
        return self.val


seq = ConstantSequence(10)
seq[0]
# 10

get_item_forgive_me(seq, 10, 'Nope')
# 10
get_item_ask_perm(seq, 10, 'Nope')
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-51-41d297dc270c> in <module>
# ----> 1 get_item_ask_perm(seq, 10, 'Nope')

# <ipython-input-44-217dce60652d> in get_item_ask_perm(seq, idx, default)
#       6         elif isinstance(idx, int):
#       7             # looks like a numerical index...
# ----> 8             if idx < len(seq):
#       9                 return seq[idx]
#      10     return default

# TypeError: object of type 'ConstantSequence' has no len()