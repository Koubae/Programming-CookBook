from enum import Enum
from functools import total_ordering
from http import HTTPStatus


class Color(Enum):
    red = 1
    green = 2
    blue = 3
    
    def purecolor(self, value):
        return {self: value}


Color.red.purecolor(100), Color.blue.purecolor(200)
# ({<Color.red: 1>: 100}, {<Color.blue: 3>: 200})

Color.red
# <Color.red: 1>


class Color(Enum):
    red = 1
    green = 2
    blue = 3
    
    def __repr__(self):
        return f'{self.name} ({self.value})'


Color.red
# red (1)

class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


try:
    Number.ONE > Number.TWO
except TypeError as ex:
    print(ex)
# '>' not supported between instances of 'Number' and 'Number'

class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

Number.ONE < Number.TWO

# True
Number.TWO > Number.ONE
# True

class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value
    
    def __eq__(self, other):
        if isinstance(other, Number):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        else:
            return False


Number.ONE == Number.ONE
# True
Number.ONE == 1.0
# False


Number.ONE == 1
# True

try:
    hash(Number.ONE)
except TypeError as ex:
    print(ex)
# unhashable type: 'Number'


class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

try:
    Number.ONE <= Number.TWO
except TypeError as ex:
    print(ex)
# '<=' not supported between instances of 'Number' and 'Number'

@total_ordering
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value


Number.ONE <= Number.TWO, Number.ONE != Number.TWO
# (True, True)

class Phase(Enum):
    READY = 'ready'
    RUNNING = 'running'
    FINISHED = 'finished'
    
    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Phase):
            return self is other
        elif isinstance(other, str):
            return self.value == other
        return False
    
    def __lt__(self, other):
        ordered_items = list(Phase)
        self_order_index = ordered_items.index(self)
        
        if isinstance(other, Phase):
            other_order_index = ordered_items.index(other)
            return self_order_index < other_order_index
        
        if isinstance(other, str):
            try:
                other_member = Phase(other)
                other_order_index = ordered_items.index(other_member)
                return self_order_index < other_order_index
            except ValueError:
                # other is not a value in our enum
                return False


Phase.READY == 'ready'
# True

Phase.READY < Phase.RUNNING
# True

Phase.READY < 'running'
# True

class State(Enum):
    READY = 1
    BUSY = 0

bool(State.READY), bool(State.BUSY)
# (True, True)

class State(Enum):
    READY = 1
    BUSY = 0    
    
    def __bool__(self):
        return bool(self.value)


bool(State.READY), bool(State.BUSY)
# (True, False)


request_state = State.READY
if request_state:
    print('Launching next query')
else:
    print('Not ready for another query yet')
# Launching next query

class Dummy(Enum):
    A = 0
    B = 1
    C = ''
    D = 'python'
    
    def __bool__(self):
        return bool(self.value)


bool(Dummy.A), bool(Dummy.B), bool(Dummy.C), bool(Dummy.D)
# (False, True, False, True)

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


try:
    class ColorAlpha(Color):
        ALPHA = 4
except TypeError as ex:
    print(ex)
# Cannot extend enumerations

class ColorBase(Enum):
    def hello(self):
        return f'{str(self)} says hello!'
    

class Color(ColorBase):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


Color.RED.hello()
# 'Color.RED says hello!'


@total_ordering
class OrderedEnum(Enum):
    """Creates an ordering based on the member values. 
    So member values have to support rich comparisons.
    """
    
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented

class Number(OrderedEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    
class Dimension(OrderedEnum):
    D1 = 1,
    D2 = 1, 1
    D3 = 1, 1, 1

Number.ONE < Number.THREE
# True

Dimension.D1 < Dimension.D3
# True

Number.ONE >= Number.ONE
# True

Dimension.D1 >= Dimension.D2
# False




type(HTTPStatus)
# enum.EnumMeta

list(HTTPStatus)[0:10]
# [<HTTPStatus.CONTINUE: 100>,
#  <HTTPStatus.SWITCHING_PROTOCOLS: 101>,
#  <HTTPStatus.PROCESSING: 102>,
#  <HTTPStatus.OK: 200>,
#  <HTTPStatus.CREATED: 201>,
#  <HTTPStatus.ACCEPTED: 202>,
#  <HTTPStatus.NON_AUTHORITATIVE_INFORMATION: 203>,
#  <HTTPStatus.NO_CONTENT: 204>,
#  <HTTPStatus.RESET_CONTENT: 205>,
#  <HTTPStatus.PARTIAL_CONTENT: 206>]

HTTPStatus(200)
# <HTTPStatus.OK: 200>

HTTPStatus.OK, HTTPStatus.OK.name, HTTPStatus.OK.value
# (<HTTPStatus.OK: 200>, 'OK', 200)


HTTPStatus(200)
# <HTTPStatus.OK: 200>

HTTPStatus['OK']
# <HTTPStatus.OK: 200>

print(HTTPStatus.NOT_FOUND.value, HTTPStatus.NOT_FOUND.name, HTTPStatus.NOT_FOUND.phrase)
# (404, 'NOT_FOUND', 'Not Found')

class AppStatus(Enum):
    OK = (0, 'No problem!')
    FAILED = (1, 'Crap!')


AppStatus.OK
# <AppStatus.OK: (0, 'No problem!')>

AppStatus.OK.value
# (0, 'No problem!')


class AppStatus(Enum):
    OK = (0, 'No problem!')
    FAILED = (1, 'Crap!')
    
    @property
    def code(self):
        return self.value[0]
    
    @property
    def phrase(self):
        return self.value[1]


AppStatus.OK.code, AppStatus.OK.phrase
# (0, 'No problem!')


try:
    AppStatus(0)
except ValueError as ex:
    print(ex)
# 0 is not a valid AppStatus

AppStatus((0, 'No problem!'))
# <AppStatus.OK: (0, 'No problem!')>



class AppStatus(Enum):
    OK = (0, 'No Problem!')
    FAILED = (1, 'Crap!')
    
    def __new__(cls, member_value, member_phrase):
        # create a new instance of cls
        member = object.__new__(cls)
        
        # set up instance attributes
        member._value_ = member_value
        member.phrase = member_phrase
        return member

print(AppStatus.OK.value, AppStatus.OK.name, AppStatus.OK.phrase)
# (0, 'OK', 'No Problem!')

AppStatus(0)
# <AppStatus.OK: 0>

class TwoValueEnum(Enum):
    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)
        member._value_ = member_value
        member.phrase = member_phrase
        return member

class AppStatus(TwoValueEnum):
    OK = (0, 'No Problem!')
    FAILED = (1, 'Crap!')

# AppStatus.FAILED, AppStatus.FAILED.name, AppStatus.FAILED.value, AppStatus.FAILED.phrase
# (<AppStatus.FAILED: 1>, 'FAILED', 1, 'Crap!')