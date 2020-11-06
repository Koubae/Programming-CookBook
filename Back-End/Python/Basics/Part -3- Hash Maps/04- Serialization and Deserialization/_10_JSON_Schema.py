import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from json import loads, dumps, JSONDecodeError
from jsonschema import Draft4Validator

# Project in Github => https://github.com/Julian/jsonschema
person_schema = {
    "type": "object",
    "properties": {
        "firstName": {"type": "string"},
        "middleInitial": {"type": "string"},
        "lastName": {"type": "string"},
        "age": {"type": "number"}
    }
}

p1 = '''
    {
        "firstName": "John",
        "middleInitial": "M",
        "lastName": "Cleese",
        "age": 79
    }
'''

p2 = '''
    {
        "firstName": "John",
        "middleInitial": 100,
        "lastName": "Cleese",
        "age": "Unknown"
    }
'''

p3 = '''
    {
        "firstName": "John",
        "age": -10.5
    }
'''



person_schema = {
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string",
            "minLength": 1
        },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
        },
        "lastName": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "integer",
            "minimum": 0
        },
        "eyeColor": {
            "type": "string",
            "enum": ["amber", "blue", "brown", "gray",
                     "green", "hazel", "red", "violet"]
        }
    },
    "required": ["firstName", "lastName"]
}


print(p1)

try:
    validate(loads(p1), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')

#  {
#         "firstName": "John",
#         "middleInitial": "M",
#         "lastName": "Cleese",
#         "age": 79
#     }
#
# JSON is valid


print(p2)

try:
    validate(loads(p2), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')

# {
#         "firstName": "John",
#         "middleInitial": 100,
#         "lastName": "Cleese",
#         "age": "Unknown"
#     }
#
# Validation error: 100 is not of type 'string'
#
# Failed validating 'type' in schema['properties']['middleInitial']:
#     {'maxLength': 1, 'minLength': 1, 'type': 'string'}
#
# On instance['middleInitial']:
#     100


print(p3)
try:
    validate(loads(p3), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')

#  {
#         "firstName": "John",
#         "age": -10.5
#     }
#
# Validation error: -10.5 is not of type 'integer'
#
# Failed validating 'type' in schema['properties']['age']:
#     {'minimum': 0, 'type': 'integer'}
#
# On instance['age']:
#     -10.5


validator = Draft4Validator(person_schema)
for error in validator.iter_errors(loads(p2)):
    print(error, end='\n-----------\n')



# 100 is not of type 'string'
#
# Failed validating 'type' in schema['properties']['middleInitial']:
#     {'maxLength': 1, 'minLength': 1, 'type': 'string'}
#
# On instance['middleInitial']:
#     100
# -----------
# 'Unknown' is not of type 'integer'
#
# Failed validating 'type' in schema['properties']['age']:
#     {'minimum': 0, 'type': 'integer'}
#
# On instance['age']:
#     'Unknown'
# -----------



p4 = '''
    {
        "firstName": "John",
        "middleInitial": null,
        "lastName": "Cleese",
        "eyeColor": "blue-gray"
    }
'''



for error in validator.iter_errors(loads(p4)):
    print(error, end='\n-----------\n')

# None is not of type 'string'
#
# Failed validating 'type' in schema['properties']['middleInitial']:
#     {'maxLength': 1, 'minLength': 1, 'type': 'string'}
#
# On instance['middleInitial']:
#     None
# -----------
# 'blue-gray' is not one of ['amber', 'blue', 'brown', 'gray', 'green', 'hazel', 'red', 'violet']
#
# Failed validating 'enum' in schema['properties']['eyeColor']:
#     {'enum': ['amber',
#               'blue',
#               'brown',
#               'gray',
#               'green',
#               'hazel',
#               'red',
#               'violet'],
#      'type': 'string'}
#
# On instance['eyeColor']:
#     'blue-gray'
# -----------

