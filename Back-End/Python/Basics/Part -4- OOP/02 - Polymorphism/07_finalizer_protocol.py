# The __del__ method as we discussed in the lecture is called right before the object is about to be garbage collected. This is sometimes called the finalizer. It is sometimes referred to as the destructor, but that's not really accurate since that method does not destroy the object - that's the GC's responsibility - __del__ just gets called prior to the GC destroying the object.

# Although this method can be useful in some circumstances we need to be aware of some pitfalls:

# Using the del keyword does not call __del__ directly - it just removes the symbol for wehatever namespace it is being deleted from and reduces the reference count by 1.
# The __del__ method is not called until the object is about to be destroyed - so using del obj decreases the ref count by 1, but if something else is referencing that object then __del__ is not called.
# Unhandled exceptions that occur in the __del__ method are essentially ignored, and the exceptions are written to sys.stderr.

import ctypes
import sys


def ref_count(address):
    return ctypes.c_long.from_address(address).value


class Person:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'Person({self.name})'
    
    def __del__(self):
        print(f'__del__ called for {self}...')

p = Person('Alex')
p = None
# __del__ called for Person(Alex)...
p = Person('Alex')
del p
# __del__ called for Person(Alex)...


class Person:
    def __init__(self, name):
        self.name = name
    
    def gen_ex(self):
        raise ValueError('Something went bump...')
        
    def __repr__(self):
        return f'Person({self.name})'
    
    def __del__(self):
        print(f'__del__ called for {self}...')

    
    
p = Person('Alex')
p_id = id(p)
ref_count(p_id)

try:
    p.gen_ex()
except ValueError as ex:
    error = ex
    print(ex)

#Something went bump...
print(ref_count(p_id)) # 2
dir(error)

# ['__cause__',
#  '__class__',
#  '__context__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__setstate__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__suppress_context__',
#  '__traceback__',
#  'args',
#  'with_traceback']

print(dir(error.__traceback__))
# ['tb_frame', 'tb_lasti', 'tb_lineno', 'tb_next']

print(dir(error.__traceback__.tb_frame))
# ['__class__',
#  '__delattr__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'clear',
#  'f_back',
#  'f_builtins',
#  'f_code',
#  'f_globals',
#  'f_lasti',
#  'f_lineno',
#  'f_locals',
#  'f_trace']
for key, value in error.__traceback__.tb_frame.f_locals.copy().items():
    if isinstance(value, Person):
        print(key, value, id(value), id(key))

#  the traceback contains a refererence to our object in it's dictionary - so we have a second reference to our object.
#p Person(Alex) 140665691193640 140665683500032

print(sys.stderr, sys.stdout)
# <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'> 
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>

class ErrToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stderr = sys.stderr
        
    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stderr = self._file
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        sys.stderr = self._current_stderr
        if self._file:
            self._file.close()
        return False

p = Person('Alex')

with ErrToFile('err.txt'):
    del p

with open('err.txt') as f:
    print(f.readlines())

p = Person('Fede')

try:
    del p
    print('p was deleted (succesfully)')
except ValueError as ex:
    print('Exception caught!')
else:
    print('No exception seen!')


# def __enter__(self)
# def __exit__(self, exc_type, exc_value, traceback)


class Package:
    def __init__(self):
        self.files = []

    def __enter__(self):
        return self

    # ...

    def __exit__(self, exc_type, exc_value, traceback):
        for file in self.files:
            os.unlink(file)

with Package() as package_obj:
    pass
    # use package_obj

# Creating a PackageResource class that defines the __enter__ and __exit__ methods. Then, the Package class would be defined strictly inside the __enter__ method and returned. That way, the caller never could instantiate the Package class without using a with statement:

class PackageResource:
    def __enter__(self):
        class Package:
            ...
        self.package_obj = Package()
        return self.package_obj

    def __exit__(self, exc_type, exc_value, traceback):
        self.package_obj.cleanup()


with Package() as package_obj:
    pass
    # use package_obj

import contextlib

@contextlib.contextmanager
def packageResource():
    class Package:
        ...
    package = Package()
    yield package
    package.cleanup()


class Package(object):
    def __new__(cls, *args, **kwargs):
        @contextlib.contextmanager
        def packageResource():
            # adapt arguments if superclass takes some!
            package = super(Package, cls).__new__(cls)
            package.__init__(*args, **kwargs)
            yield package
            package.cleanup()

    def __init__(self, *args, **kwargs):
        ...

    class Package(object):
    def __new__(cls, *args, **kwargs):
        package = super(Package, cls).__new__(cls)
        package.__init__(*args, **kwargs)
        return contextlib.closing(package)

class SubPackage(Package):
    def close(self):
        pass
