from fractions import Fraction
import json
from datetime import datetime
from decimal import Decimal


j = '''
    {
        "time": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:15"
            },
        "message": "created this json string"
    }
'''




def custom_decoder(arg):
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
    else:
        return arg  # important, otherwise we lose anything that's not a date!

d = json.loads(j, object_hook=custom_decoder)
print(d)
# {'time': datetime.datetime(2018, 10, 21, 9, 14, 15), 'message': 'created this json string'}

for key, value in d.items():
    if (isinstance(value, dict) and
        'objecttype' in value and
        value['objecttype'] == 'fraction'):
        numerator = value['numerator']
        denominator = value['denominator']
        d[key] = Fraction(numerator, denominator)


def custom_decoder(arg):
    print('decoding: ', arg)
    return arg

j = '''
    {
        "a": 1,
        "b": 2, 
        "c": {
            "c.1": 1,
            "c.2": 2,
            "c.3": {
                "c.3.1": 1,
                "c.3.2": 2
            }
        }
    }
'''
d = json.loads(j, object_hook=custom_decoder)
# decoding:  {'c.3.1': 1, 'c.3.2': 2}
# decoding:  {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}
# decoding:  {'a': 1, 'b': 2, 'c': {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}}


def custom_decoder(arg):
    ret_value = arg
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            ret_value = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            ret_value = Fraction(arg['numerator'], arg['denominator'])
    return ret_value



j = '''
    {
        "cake": "yummy chocolate cake",
        "myShare": {
            "objecttype": "fraction",
            "numerator": 1,
            "denominator": 8
        },
        "eaten": {
            "at": {
                "objecttype": "datetime",
                "value": "2018-10-21T21:30:00"
                },
            "time_taken": "30 seconds"
        }
    }
'''

d = json.loads(j, object_hook=custom_decoder)
print(d)
# {'cake': 'yummy chocolate cake', 'myShare': Fraction(1, 8),
# 'eaten': {'at': datetime.datetime(2018, 10, 21, 21, 30),
# 'time_taken': '30 seconds'}}


class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'


j = '''
    {
        "accountHolder": {
            "objecttype": "person",
            "name": "Eric Idle",
            "ssn": 100
        },
        "created": {
            "objecttype": "datetime",
            "value": "2018-10-21T03:00:00"
        }
    }
'''



def custom_decoder(arg):
    ret_value = arg
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            ret_value = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            ret_value = Fraction(arg['numerator'], arg['denominator'])
        elif arg['objecttype'] == 'person':
            ret_value = Person(arg['name'], arg['ssn'])
    return ret_value


d = json.loads(j, object_hook=custom_decoder)
print(d)
# {'accountHolder': Person(name=Eric Idle, ssn=100),
#  'created': datetime.datetime(2018, 10, 21, 3, 0)}

class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'

    def toJSON(self):
        return dict(objecttype='person', name=self.name, ssn=self.ssn)


def make_decimal(arg):
    print('Received:', type(arg), arg)
    return Decimal(arg)


j = '''
    {
        "a": 100,
        "b": 0.2,
        "c": 0.5
    }
'''
d = json.loads(j, parse_float=make_decimal)
print(d)
# {'a': 100, 'b': Decimal('0.2'), 'c': Decimal('0.5')}



def make_int_binary(arg):
    print('Received:', type(arg), arg)
    return bin(int(arg))


def make_const_none(arg):
    print('Received:', type(arg), arg)
    return None
json.loads(j,
           parse_int=make_int_binary,
           parse_constant=make_const_none)


# Received: <class 'str'> 100
# Received: <class 'str'> Infinity
# {'a': '0b1100100', 'b': None}



j = '''
    {
        "a": [1, 2, 3, 4, 5],
        "b": 100,
        "c": 10.5,
        "d": NaN,
        "e": null,
        "f": "python"
    }
'''


def float_handler(arg):
    print('float handler', type(arg), arg)
    return float(arg)


def int_handler(arg):
    print('int handler', type(arg), arg)
    return int(arg)


def const_handler(arg):
    print('const handler', type(arg), arg)
    return None


def obj_hook(arg):
    print('obj hook', type(arg), arg)
    return arg


def obj_pairs_hook(arg):
    print('obj pairs hook', type(arg), arg)
    return arg

print(json.loads(j))
# {'a': [1, 2, 3, 4, 5], 'b': 100, 'c': 10.5,
# 'd': nan, 'e': None, 'f': 'python'}
print(json.loads(j,
           object_hook=obj_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          ))


#
# int handler <class 'str'> 1
# int handler <class 'str'> 2
# int handler <class 'str'> 3
# int handler <class 'str'> 4
# int handler <class 'str'> 5
# int handler <class 'str'> 100
# float handler <class 'str'> 10.5
# const handler <class 'str'> NaN
# obj hook <class 'dict'> {'a': [1, 2, 3, 4, 5], 'b': 100, 'c': 10.5, 'd': None, 'e': None, 'f': 'python'}
#
#
# {'a': [1, 2, 3, 4, 5],
#  'b': 100,
#  'c': 10.5,
#  'd': None,
#  'e': None,
#  'f': 'python'}



json.loads(j,
           object_pairs_hook=obj_pairs_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          )


# int handler <class 'str'> 1
# int handler <class 'str'> 2
# int handler <class 'str'> 3
# int handler <class 'str'> 4
# int handler <class 'str'> 5
# int handler <class 'str'> 100
# float handler <class 'str'> 10.5
# const handler <class 'str'> NaN
# obj pairs hook <class 'list'> [('a', [1, 2, 3, 4, 5]), ('b', 100), ('c', 10.5), ('d', None), ('e', None), ('f', 'python')]
#
# [('a', [1, 2, 3, 4, 5]),
#  ('b', 100),
#  ('c', 10.5),
#  ('d', None),
#  ('e', None),
#  ('f', 'python')]


json.loads(j,
           object_hook=obj_hook,
           object_pairs_hook=obj_pairs_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          )

#
#
# int handler <class 'str'> 1
# int handler <class 'str'> 2
# int handler <class 'str'> 3
# int handler <class 'str'> 4
# int handler <class 'str'> 5
# int handler <class 'str'> 100
# float handler <class 'str'> 10.5
# const handler <class 'str'> NaN
# obj pairs hook <class 'list'> [('a', [1, 2, 3, 4, 5]), ('b', 100), ('c', 10.5), ('d', None), ('e', None), ('f', 'python')]
#
#
#
# [('a', [1, 2, 3, 4, 5]),
#  ('b', 100),
#  ('c', 10.5),
#  ('d', None),
#  ('e', None),
#  ('f', 'python')]

