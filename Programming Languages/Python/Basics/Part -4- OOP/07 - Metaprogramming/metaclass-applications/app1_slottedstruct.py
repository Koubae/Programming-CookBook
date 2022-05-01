class Point2D:
    __slots__ = ('_x', '_y')
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'
    
    def __str__(self):
        return f'({self.x}, {self.y})'
        
class Point3D:
    __slots__ = ('_x', '_y', '_z')
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f'Point2D({self.x}, {self.y}, {self.z})'
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


class Point2D:
    _fields = ['x', 'y']
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
class Point3D:
    _fields = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z



class SlottedStruct(type):
    def __new__(cls, name, bases, class_dict):
        cls_object = super().__new__(cls, name, bases, class_dict)
        
        # setup the __slots__
        setattr(cls_object, '__slots__', [f'_{field}' for field in cls_object._fields])
            
        # create read-only property for each field
        for field in cls_object._fields:
            slot = f'_{field}'
            # this will not work!
            #     setattr(cls_object, field, property(fget=lambda self: getattr(self, slot)))
            # Remember about how closures work! The free variable is resolved when the function is called!
            # So instead we have to use this workaround, by specifying the slot as a defaulted argument
            setattr(cls_object, field, property(fget=lambda self, attrib=slot: getattr(self, attrib)))

        # create __eq__ method
        def eq(self, other):
            if isinstance(other, cls_object):
                # ensure each corresponding field is equal
                self_fields = [getattr(self, field) for field in cls_object._fields]
                other_fields = [getattr(other, field) for field in cls_object._fields]
                return self_fields == other_fields
            return False
        setattr(cls_object, '__eq__', eq)

        # create __hash__ method
        def hash_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            return hash(tuple(field_values))
        setattr(cls_object, '__hash__', hash_)
        
        # create __str__ method
        def str_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            field_values_joined = ', '.join(map(str, field_values))  # make every value a string
            return f'{cls_object.__name__}({field_values_joined})'
        setattr(cls_object, '__str__', str_)
        
        # create __repr__ method
        def repr_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            field_key_values = (f'{key}={value}' for key, value in zip(cls_object._fields, field_values))
            field_key_values_str = ', '.join(field_key_values)
            return f'{cls_object.__name__}({field_key_values_str})'
        setattr(cls_object, '__repr__', repr_)
        
        return cls_object

class Person(metaclass=SlottedStruct):
    _fields = ['name']
    
    def __init__(self, name):
        self._name = name

print(type(Person))
print(type(p1), isinstance(p1, Person))


class Point2D(metaclass=SlottedStruct):
    _fields = ['x', 'y']
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
class Point3D(metaclass=SlottedStruct):
    _fields = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

p1 = Point2D(1, 2)
p2 = Point2D(1, 2)
p3 = Point2D(0, 0)


repr(p1), str(p1), hash(p1), p1.x, p1.y
# ('Point2D(x=1, y=2)', 'Point2D(1, 2)', 3713081631934410656, 1, 2)

repr(p2), str(p2), hash(p2), p2.x, p2.y
# ('Point2D(x=1, y=2)', 'Point2D(1, 2)', 3713081631934410656, 1, 2)
p1 is p2, p1 == p2


# (False, True)


p1 is p3, p1 == p3
# (False, False)

p1 = Point3D(1, 2, 3)
p2 = Point3D(1, 2, 3)
p3 = Point3D(0, 0, 0)
p1.x, p1.y, p1.z


# (1, 2, 3)

p1 == p2, p1 == p3

# (True, False)



print(Point2D.__name__, Point2D.__bases__, Point2D.__dict__)


# ('Point2D',
#  (object,),
#  mappingproxy({'__module__': '__main__',
#                '_fields': ['x', 'y'],
#                '__init__': <function __main__.Point2D.__init__(self, x, y)>,
#                '__dict__': <attribute '__dict__' of 'Point2D' objects>,
#                '__weakref__': <attribute '__weakref__' of 'Point2D' objects>,
#                '__doc__': None,
#                '__slots__': ['_x', '_y'],
#                'x': <property at 0x7fc7d0256778>,
#                'y': <property at 0x7fc7d02567c8>,
#                '__eq__': <function __main__.SlottedStruct.__new__.<locals>.eq(self, other)>,
#                '__hash__': <function __main__.SlottedStruct.__new__.<locals>.hash_(self)>,
#                '__str__': <function __main__.SlottedStruct.__new__.<locals>.str_(self)>,
#                '__repr__': <function __main__.SlottedStruct.__new__.<locals>.repr_(self)>}))



def struct(cls):
    return SlottedStruct(cls.__name__, cls.__bases__, dict(cls.__dict__))


@struct
class Point2D:
    _fields = ['x', 'y']
    
    def __init__(self, x, y):
        self._x = x
        self._y = y


type(Point2D)
# __main__.SlottedStruct
p = Point2D(1, 2)
type(p)
# __main__.Point2D
p.x, p.y
# (1, 2)
repr(p)
# 'Point2D(x=1, y=2)'