class AppException(Exception):
    """generic application exception"""
    
class NegativeIntegerError(AppException):
    """Used to indicate an error when an integer is negative."""


def set_age(age):
    if age < 0:
        raise NegativeIntegerError('age cannot be negative')


try:
    set_age(-10)
except NegativeIntegerError as ex:
    print(repr(ex))
# NegativeIntegerError('age cannot be negative',)



class BaseClass1:
    pass

class BaseClass2:
    pass

class MyClass(BaseClass1, BaseClass2):
    pass


issubclass(MyClass, BaseClass1)
# True
issubclass(MyClass, BaseClass2)
# True

class NegativeIntegerError(AppException, ValueError):
    """Used to indicate an error when an integer is negative."""
Now this exception is a subclass of both AppException and ValueError:


issubclass(NegativeIntegerError, AppException)
# True

issubclass(NegativeIntegerError, ValueError)
# True

def set_age(age):
    if age < 0:
        raise NegativeIntegerError('age cannot be negative')

try:
    set_age(-10)
except NegativeIntegerError as ex:
    print(repr(ex))
# NegativeIntegerError('age cannot be negative',)

try:
    set_age(-10)
except ValueError as ex:
    print(repr(ex))
# NegativeIntegerError('age cannot be negative',)
