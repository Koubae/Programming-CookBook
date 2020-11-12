import enum
import json

class Color(enum.Enum):
    red = 1
    green = 2
    blue = 3


class Status(enum.Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'


class UnitVector(enum.Enum):
    V1D = (1, )
    V2D = (1, 1)
    V3D = (1, 1, 1)

Status.PENDING
# <Status.PENDING: 'pending'>
type(Status.PENDING)
# <enum 'Status'>
isinstance(Status.PENDING, Status)
# True

Status.PENDING.name, Status.PENDING.value
('PENDING', 'pending')

Status.PENDING is Status.PENDING
Out[9]:
# True
Status.PENDING == Status.PENDING
# True

class Constants(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
try:
    Constants.ONE > Constants.TWO
except TypeError as ex:
    print(ex)
# '>' not supported between instances of 'Constants' and 'Constants'

Status.PENDING in Status
# True

Status.PENDING.name, Status.PENDING.value
# ('PENDING', 'pending')

'PENDING' in Status, 'pending' in Status
# (False, False)

Status('pending'), UnitVector((1,1))
# (<Status.PENDING: 'pending'>, <UnitVector.V2D: (1, 1)>)

try:
    Status('invalid')
except ValueError as ex:
    print(ex)
# 'invalid' is not a valid Status

class Person:
    def __getitem__(self, val):
        return f'__getitem__({val}) called...'

p = Person()

p['some value']
# '__getitem__(some value) called...'

hasattr(Status, '__getitem__')
# True

Status['PENDING']
# <Status.PENDING: 'pending'>

getattr(Status, 'PENDING')
# <Status.PENDING: 'pending'>

class Person:
    __hash__ = None

p = Person()

try:
    hash(p)
except TypeError as ex:
    print(ex)
# unhashable type: 'Person'

class Family(enum.Enum):
    person_1 = Person()
    person_2 = Person()
Family.person_1
# <Family.person_1: <__main__.Person object at 0x7fbb083d1320>>

# {
    # Family.person_1: 'person 1',
    # Family.person_2: 'person 2'
# }
# {<Family.person_1: <__main__.Person object at 0x7fbb083d1320>>: 'person 1',
#  <Family.person_2: <__main__.Person object at 0x7fbb083d1390>>: 'person 2'}

hasattr(Status, '__iter__')
# True

for member in Status:
    print(repr(member))
# <Status.PENDING: 'pending'>
# <Status.RUNNING: 'running'>
# <Status.COMPLETED: 'completed'>

class Numbers1(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
class Numbers2(enum.Enum):
    THREE = 3
    TWO = 2
    ONE = 1
list(Numbers1)
# [<Numbers1.ONE: 1>, <Numbers1.TWO: 2>, <Numbers1.THREE: 3>]
list(Numbers2)
# [<Numbers2.THREE: 3>, <Numbers2.TWO: 2>, <Numbers2.ONE: 1>]

try:
    Status.PENDING.value = 10
except AttributeError as ex:
    print(ex)
# can't set attribute

try:
    Status['NEW'] = 100
except TypeError as ex:
    print(ex)
# 'EnumMeta' object does not support item assignment

class EnumBase(enum.Enum):
    pass

class EnumExt(EnumBase):
    ONE = 1
    TWO = 2

EnumExt.ONE
# <EnumExt.ONE: 1>


class EnumBase(enum.Enum):
    ONE = 1

try:
    class EnumExt(EnumBase):
        TWO = 2
except TypeError as ex:
    print(ex)

Status.PENDING, Status['PENDING']
# (<Status.PENDING: 'pending'>, <Status.PENDING: 'pending'>)

payload = """
{
  "name": "Alex",
  "status": "PENDING"
}
"""



data = json.loads(payload)

data['status']
# 'PENDING'


Status[data['status']]
# <Status.PENDING: 'pending'>

def is_member(en, name):
    try:
        en[name]
    except KeyError:
        return False
    return True

is_member(Status, 'PENDING')
# True

is_member(Status, 'pending')
# False


getattr(Status, 'PENDING', None), getattr(Status, 'OK', None)
# (<Status.PENDING: 'pending'>, None)


Status.__members__

# 'PENDING' in Status.__members__
# True
# 'PENDING' in Status.__members__.keys()

# True