# Single Dispatch
=======================



Because the name of the individual specialized functions does not really matter to us (the dispatcher will pick the appropriate function), it is quite common for an underscore character ( _ ) to be used for the function name - the memory address of each specialized function will be stored in the registry dictionary, and the function name does not matter - in fact we can even add lambdas to the registry.

```

@singledispatch
def htmlize(a):
    return escape(str(a))

    
@htmlize.register(int)
def _(a):
    return '{0}({1})'.format(a, str(hex(a)))

```

- [DOCS](https://docs.python.org/3/glossary.html#term-single-dispatch)

A form of generic function dispatch where the implementation is chosen based on the type of a single argument.



-----------------------------------------------------------------------------------------------------

## Features

- Single Dispatch & Multi dispatch.

[PEP 443](https://www.python.org/dev/peps/pep-0443/)
[Function Overloading with singledispatchhttps](https://www.blog.pythonlibrary.org/2016/02/23/python-3-function-overloading-with-singledispatch/)

- [generic function](https://docs.python.org/3/glossary.html#term-generic-function)


### Modules

- [functools singledispatch](https://docs.python.org/3/library/functools.html#functools.singledispatch)
- [numbers.Integral](https://docs.python.org/3.8/library/numbers.html#numbers.Integral)
- [collections.abc.Sequence](https://docs.python.org/3.8/library/collections.abc.html#collections.abc.Sequence)

### 

- [singledispatch 3.4.0.3](https://pypi.org/project/singledispatch/)

-----------------------------------------------------------------------------------------------------