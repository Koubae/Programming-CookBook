import inspect


def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
    """Calculates the factorial of a non-negative integer n

    If n is negative, returns 0.
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n - 1)


def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

class MyClass:
    # Instance methods are bound to the instance of a class (not the class itself)
    def f_instance(self):
        pass
    # Class methods are bound to the class, not instances
    @classmethod
    def f_class(cls):
        pass
    # Static methods are no bound either to the class or its instances
    @staticmethod
    def f_static():
        pass

inspect.isfunction(MyClass.f_instance), inspect.ismethod(MyClass.f_instance)
# (True, False)
inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class)
# (False, True)
inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static)
# (True, False)

my_obj = MyClass()
inspect.isfunction(my_obj.f_instance), inspect.ismethod(my_obj.f_instance)
# (False, True)
inspect.isfunction(my_obj.f_class), inspect.ismethod(my_obj.f_class)
# (False, True)
inspect.isfunction(my_obj.f_static), inspect.ismethod(my_obj.f_static)
# (True, False)

####  If you just want to know if something is a function or method:
inspect.isroutine(my_func)
inspect.isroutine(MyClass.f_instance)
inspect.isroutine(my_obj.f_class)
inspect.isroutine(my_obj.f_static)
# All True


# We can get back the source code of our function using the getsource() method:
print(inspect.getsource(fact))
# def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
#     """Calculates the factorial of a non-negative integer n
#
#     If n is negative, returns 0.
#     """
#     if n < 0:
#         return 0
#     elif n <= 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# Process finished with exit code 0
inspect.getsource(MyClass.f_instance)
inspect.getsource(my_obj.f_instance)
inspect.getmodule(fact)
inspect.getmodule(print)

import math

inspect.getmodule(math.sin)

# setting up variable
i = 10

# comment line 1
# comment line 2
def my_func(a, b=1):
    # comment inside my_func
    pass
inspect.getcomments(my_func)
print(inspect.getcomments(my_func))


# TODO: Provide implementation
def my_func(a: 'a string',
            b: int = 1,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg' = 10,
            **kwargs: 'additional keyword-only args') -> str:
    """does something
       or other"""
    pass

inspect.signature(my_func)
type(inspect.signature(my_func))
sig = inspect.signature(my_func)
dir(sig)
for param_name, param in sig.parameters.items():
    print(param_name, param)


def print_info(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')

    print('{0}\n{1}\n'.format(inspect.getcomments(f),
                              inspect.cleandoc(f.__doc__)))

    print('{0}\n{1}'.format('Inputs', '-' * len('Inputs')))

    sig = inspect.signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('--------------------------\n')

    print('{0}\n{1}'.format('\n\nOutput', '-' * len('Output')))
    print(sig.return_annotation)

# my_func
# =======
#
# # TODO: Provide implementation
#
# does something
# or other
#
# Inputs
# ------
# Name: a
# Default: <class 'inspect._empty'>
# Annotation: a string
# Kind: POSITIONAL_OR_KEYWORD
# --------------------------
#
# Name: b
# Default: 1
# Annotation: <class 'int'>
# Kind: POSITIONAL_OR_KEYWORD
# --------------------------
#
# Name: args
# Default: <class 'inspect._empty'>
# Annotation: additional positional args
# Kind: VAR_POSITIONAL
# --------------------------
#
# Name: kw1
# Default: <class 'inspect._empty'>
# Annotation: first keyword-only arg
# Kind: KEYWORD_ONLY
# --------------------------
#
# Name: kw2
# Default: 10
# Annotation: second keyword-only arg
# Kind: KEYWORD_ONLY
# --------------------------
#
# Name: kwargs
# Default: <class 'inspect._empty'>
# Annotation: additional keyword-only args
# Kind: VAR_KEYWORD
# --------------------------
