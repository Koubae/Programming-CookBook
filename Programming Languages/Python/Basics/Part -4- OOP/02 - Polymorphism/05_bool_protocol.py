class MyList:
    def __init__(self, length):
        self._length = length
        
    def __len__(self):
        print('__len__ called')
        return self._length
    
    def __bool__(self):
        print('__bool__ called')
        return self._length > 0


p1 = MyList(0)
p2 = MyList(100)
print(bool(p1))
# __bool__ called

# False
print(bool(p2))
# __bool__ called

# True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(0, 0)
p2 = Point(1, 1)

print(bool(p1), bool(p2))
# (True, True)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __bool__(self):
        return self.x or self.y



p1 = Point(0, 0)
p2 = Point(1, 1)
print(bool(p1.__bool__()), bool(p2.__bool__()))
try:
    bool(p1)
except TypeError as ex:
    print(ex)
# __bool__ should return bool, returned int



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __bool__(self):
        return bool(self.x or self.y)

p1 = Point(0, 0)
p2 = Point(1, 1)

bool(p1), bool(p2)
#(False, True)