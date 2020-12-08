from functools import cached_property

class cached_property(object):
    """
    Decorator that converts a method with a single self argument into a
    property cached on the instance.
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, type=None):
        if instance is None:
            return self
        res = instance.__dict__[self.func.__name__] = self.func(instance)
        return res




# Example 2

def test_cached_property(self):
        """cached_property caches its value and behaves like a property."""
        class Class:
            @cached_property
            def value(self):
                """Here is the docstring..."""
                return 1, object()

            @cached_property
            def __foo__(self):
                """Here is the docstring..."""
                return 1, object()

            def other_value(self):
                """Here is the docstring..."""
                return 1, object()

            other = cached_property(other_value, name='other')

        attrs = ['value', 'other', '__foo__']
        for attr in attrs:
            self.assertCachedPropertyWorks(attr, Class)




# https://stackoverflow.com/questions/62160411/pythons-new-functools-cached-property-bug-or-limitation
class lazyprop:
    """Based on code from David Beazley's "Python Cookbook"."""
    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = instance.__dict__[self.func.__name__] = self.func(instance)
            return value

class D:
    def __init__(self, greeting='Hello'):
        self.greeting = greeting

def greet(self):
    return self.greeting + " world!"


# Beazley's version works...
D.greet = lazyprop(greet)
assert D().greet == "Hello world!"

# ... but the builtin version will fail
D.greet = cached_property(greet)
# D().greet  # this will fail

D.greet = cached_property(greet)
D.greet.__set_name__(D, 'greet')  # sets D.greet.attrname = "greet" for later use

assert D().greet == "hello world!"