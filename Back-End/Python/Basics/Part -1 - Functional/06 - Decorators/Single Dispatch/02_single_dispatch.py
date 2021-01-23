from html import escape



def singledispatch(fn):
    registry = dict()

    registry[object] = fn
    registry[int] = lambda arg: '{0}(<i>{1}</i)'.format(arg, str(hex(arg)))
    registry[float] = lambda arg: '{0:.2f}'.format(round(arg, 2))

    def inner(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    return inner

@singledispatch
def htmlizer(a):
    return escape(str(a))

print(htmlizer('a < 10'))
print(htmlizer(10))
print(htmlizer(3.1415))





