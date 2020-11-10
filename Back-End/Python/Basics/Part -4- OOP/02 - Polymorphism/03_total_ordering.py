from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other):
        print('__eq__ called...')
        if isinstance(other, Number):
            return self.x == other.x
        return NotImplemented
    
    def __lt__(self, other):
        print('__lt__ called...')
        if isinstance(other, Number):
            return self.x < other.x
        return NotImplemented

a = Number(1)
b = Number(2)
c = Number(1)
print(a < b)
print(a <= b)
print(a <= c)