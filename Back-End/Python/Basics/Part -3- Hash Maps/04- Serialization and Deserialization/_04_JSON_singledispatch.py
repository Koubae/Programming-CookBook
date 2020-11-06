import json
from datetime import datetime


log_record = {
    'time': datetime.utcnow(),
    'message': 'Testing...',
    'other': {'a', 'b', 'c'}
}


def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)

print(json.dumps(log_record, default=custom_json_formatter))
#{"time": "2020-11-06T03:10:44.482803", "message": "Testing...", "other": ["a", "b", "c"]}

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt.isoformat()
        }

p = Person('John', 82)
print(p)
print(p.toJSON())
# {"time": "2020-11-06T03:11:08.677000", "message": "Testing...", "other": ["b", "a", "c"]}
# Person(name=John, age=82)
# {'name': 'John', 'age': 82, 'create_dt': '2020-11-06T03:11:08.677000'}

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    elif isinstance(arg, Person):
        return arg.toJSON()

log_record = dict(time=datetime.utcnow(),
                  message='Created new person record',
                  person=p)

print(json.dumps(log_record, default=custom_json_formatter, indent=2))

# {
#   "time": "2020-11-06T03:12:12.624757",
#   "message": "Created new person record",
#   "person": {
#     "name": "John",
#     "age": 82,
#     "create_dt": "2020-11-06T03:12:12.624757"
#   }
# }

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt
        }

p = Person('Monty', 100)
log_record = dict(time=datetime.utcnow(),
                  message='Created new person record',
                  person=p)

print(json.dumps(log_record, default=custom_json_formatter, indent=2))

# {
#   "time": "2020-11-06T03:13:01.412670",
#   "message": "Created new person record",
#   "person": {
#     "name": "Monty",
#     "age": 100,
#     "create_dt": "2020-11-06T03:13:01.412670"
#   }
# }

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return vars(self)

p = Person('Python', 27)
print(p.toJSON())
# {'name': 'Python', 'age': 27, 'create_dt': datetime.datetime(2020, 11, 6, 3, 13, 34, 452006)}
log_record['person'] = p
print(log_record)
#{'time': datetime.datetime(2020, 11, 6, 3, 14, 6, 399677), 'message': 'Created new person record', 'person': Person(name=Python, age=27)}
print(json.dumps(log_record, default=custom_json_formatter, indent=2))

# {
#   "time": "2020-11-06T03:14:19.885341",
#   "message": "Created new person record",
#   "person": {
#     "name": "Python",
#     "age": 27,
#     "create_dt": "2020-11-06T03:14:19.885341"
#   }
# }

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    else:
        try:
            return arg.toJSON()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

pt1 = Point(10, 10)

log_record = dict(time=datetime.utcnow(),
                  message='Created new point',
                  point=pt1,
                  created_by=p)

print(json.dumps(log_record, default=custom_json_formatter, indent=2))

# {
#   "time": "2020-11-06T03:18:39.272100",
#   "message": "Created new point",
#   "point": {
#     "x": 10,
#     "y": 10
#   },
#   "created_by": {
#     "name": "Python",
#     "age": 27,
#     "create_dt": "2020-11-06T03:18:39.272100"
#   }
# }
