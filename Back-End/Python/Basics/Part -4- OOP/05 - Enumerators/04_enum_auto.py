import enum


class State(enum.Enum):
    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()



for member in State:
    print(member.name, member.value)
# WAITING 1
# STARTED 2
# FINISHED 3


class State(enum.Enum):
    WAITING = 5
    STARTED = enum.auto()
    FINISHED = enum.auto()
for member in State:
    print(member.name, member.value)
# WAITING 5
# STARTED 6
# FINISHED 7

class State(enum.Enum):
    WAITING = enum.auto()
    STARTED = 1
    FINISHED = enum.auto()
    
for member in State:
    print(member.name, member.value)
    
# State.__members__
# WAITING 1
# FINISHED 2
# mappingproxy({'WAITING': <State.WAITING: 1>,
#               'STARTED': <State.WAITING: 1>,
#               'FINISHED': <State.FINISHED: 2>})


try:
    @enum.unique
    class State(enum.Enum):
        WAITING = enum.auto()
        STARTED = 1
        FINISHED = enum.auto()
except ValueError as ex:
    print(ex)
# duplicate values found in <enum 'State'>: STARTED -> WAITING


class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(name, start, count, last_values)
        return 100
    
    a = enum.auto()
    b = enum.auto()
    c = enum.auto()


# a 1 0 []
# b 1 1 [100]
# c 1 2 [100, 100]


import random

random.seed(0)

class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            new_value = random.randint(1, 100)
            if new_value not in last_values:
                return new_value
            
    a = enum.auto()
    b = enum.auto()
    c = enum.auto()


for member in State:
    print(member.name, member.value)
# a 50
# b 98
# c 54

class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()  
    
    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()

    
for member in State:
    print(member.name, member.value)
# WAITING Waiting
# STARTED Started
# FINISHED Finished


class NameAsString(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class Enum1(NameAsString):
    A = enum.auto()
    B = enum.auto()
    

class Enum2(NameAsString):
    WAIT = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()


for member in Enum1:
    print(member.name, member.value)
    
for member in Enum2:
    print(member.name, member.value)
# A a
# B b
# WAIT wait
# RUNNING running
# FINISHED finished




class State(enum.Enum):
    WAIT = object()
    RUNNING = object()
    FINISHED = object()


State.WAIT, State.RUNNING, State.FINISHED
# (<State.WAIT: <object object at 0x7fab7807bd30>>,
#  <State.RUNNING: <object object at 0x7fab7807bd40>>,
#  <State.FINISHED: <object object at 0x7fab7807bda0>>)


class ValuelessEnum(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return object()
    
class State(ValuelessEnum):
    WAIT = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()
    
class Errors(ValuelessEnum):
    NumberError = enum.auto()
    IndexError = enum.auto()
    TimeoutError = enum.auto()


State.WAIT, Errors.TimeoutError
# (<State.WAIT: <object object at 0x7fab7807bdd0>>,
#  <Errors.TimeoutError: <object object at 0x7fab7807be40>>)

class ValuelessEnum(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            new_value = random.randint(1, 100)
            if new_value not in last_values:
                return new_value
    
class State(ValuelessEnum):
    WAIT = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()


class Errors(ValuelessEnum):
    NumberError = enum.auto()
    IndexError = enum.auto()
    TimeoutError = enum.auto()


State.WAIT, Errors.TimeoutError
# (<State.WAIT: 6>, <Errors.TimeoutError: 39>)



class Aliased(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(f'count={count}')
        if count % 2 == 1:
            # odd, make this member an alias of the previous one
            return last_values[-1]
        else:
            # make a new value
            return last_values[-1] + 1
       
    GREEN = 1
    GREEN_ALIAS = 1
    RED = 10
    CRIMSON = enum.auto()
    BLUE = enum.auto()
    AQUA = enum.auto()


count=3
count=4
count=5

list(Aliased)
# [<Aliased.GREEN: 1>, <Aliased.RED: 10>, <Aliased.BLUE: 11>]
Aliased.__members__

# mappingproxy({'GREEN': <Aliased.GREEN: 1>,
#               'GREEN_ALIAS': <Aliased.GREEN: 1>,
#               'RED': <Aliased.RED: 10>,
#               'CRIMSON': <Aliased.RED: 10>,
#               'BLUE': <Aliased.BLUE: 11>,
#               'AQUA': <Aliased.BLUE: 11>})