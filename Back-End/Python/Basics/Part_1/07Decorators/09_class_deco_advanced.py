from functools import total_ordering
from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0,0)

print(p1, p2, p1==p2) # Point(2, 3) Point(2, 3) True
p4 = Point(1, 2)
print(p1 > p4) # True


# Now, although we could proceed in a similar way and define >=, <= and > using the same technique, observe that if < and == is defined then:
#
# a <= b if a < b or a == b
# a > b if not(a<b) and a != b
# a >= b if not(a<b)

def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    return cls

# def ge_from_lt(self, other):
#     # self >= other iff not(other < self)
#     result = self.__lt__(other)
#     if result is NotImplemented:
#         return NotImplemented
#     else:
#         return not result

# Now the complete_ordering decorator can also be directly applied to any class that defines __eq__ and __lt__.

@complete_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)

    def __repr__(self):
        return f'Grade({self.score}, {self.max_score})'

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented


g1 = Grade(10, 100)
g2 = Grade(20, 30)
g3 = Grade(5, 50)
print(g1 <= g2, g1 == g3, g2 > g3) # True True True


# PythonDecorators/decorator_with_arguments.py
class decorator_with_arguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

@decorator_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")

