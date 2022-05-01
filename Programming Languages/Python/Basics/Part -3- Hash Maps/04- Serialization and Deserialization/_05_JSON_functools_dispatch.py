from functools import singledispatch
import json
from datetime import datetime
from decimal import Decimal
from fractions import Fraction


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


@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON...')
        return arg.toJSON()
    except AttributeError:
        print('\tfailed - trying to use vars...')
        try:
            return vars(arg)
        except TypeError:
            print('\tfailed - using string representation...')
            return str(arg)


@json_format.register(datetime)
def _(arg):
    return arg.isoformat()


@json_format.register(set)
def _(arg):
    return list(arg)


print(json.dumps(log_record, default=json_format, indent=2))

# Point(x=10, y=10)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# {
#   "time": "2020-11-06T03:20:55.165715",
#   "message": "Created new point",
#   "point": {
#     "x": 10,
#     "y": 10
#   },
#   "created_by": {
#     "name": "Python",
#     "age": 27,
#     "create_dt": "2020-11-06T03:20:55.165715"
#   }
# }

print(json.dumps(dict(a=1+1j,
                b=Decimal('0.5'),
                c=Fraction(1, 3),
                p=Person('Python', 27),
                pt=Point(0,0),
                time=datetime.utcnow()
               ),
           default=json_format))


# (1+1j)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# 0.5
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# 1/3
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# Point(x=0, y=0)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# {"a": "(1+1j)", "b": "0.5", "c": "1/3", "p": {"name": "Python", "age": 27, "create_dt": "2020-11-06T03:21:55.031736"}, "pt": {"x": 0, "y": 0}, "time": "2020-11-06T03:21:55.031736"}
#
@json_format.register(Decimal)
def _(arg):
    return f'Decimal({str(arg)})'
print('==='*15)
print(json.dumps(dict(a=1+1j,
                b=Decimal(0.5),
                c=Fraction(1, 3),
                p=Person('Python', 27),
                pt = Point(0,0),
                time = datetime.utcnow()
               ),
           default=json_format))

# (1+1j)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# 1/3
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# Point(x=0, y=0)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# {"a": "(1+1j)", "b": "Decimal(0.5)", "c": "1/3", "p": {"name": "Python", "age": 27, "create_dt": "2020-11-06T03:23:06.138878"}, "pt": {"x": 0, "y": 0}, "time": "2020-11-06T03:23:06.138878"}
# Point(x=Person(name=Python, age=27), y=(2+2j))
# 	trying to use toJSON...
# 	failed - trying to use vars...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# (2+2j)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...

print(json.dumps(dict(pt = Point(Person('Python', 27), 2+2j)),
          default=json_format, indent=2))

# {
#   "pt": {
#     "x": {
#       "name": "Python",
#       "age": 27,
#       "create_dt": "2020-11-06T03:22:40.225578"
#     },
#     "y": "(2+2j)"
#   }
# }
