from html import escape


def singledispatch(fn):

    registry = dict()
    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!
        return inner

    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorator.register = register
    decorator.registry = registry.keys()
    decorator.reg_item = registry.items()
    decorator.dispatch = dispatch
    return decorator

@singledispatch
def htmlize(arg):
    return escape(str(arg))

print(htmlize.registry)
print(htmlize.reg_item)
# dict_keys([<class 'object'>])
# dict_items([(<class 'object'>, <function htmlize at 0x0000021D1D963CA0>)])
print(htmlize.register)
print(htmlize.dispatch(str))
print(htmlize.dispatch(int))

@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

print(htmlize.registry)
print(htmlize.reg_item)
# dict_keys([<class 'object'>, <class 'int'>])
# dict_items([(<class 'object'>, <function htmlize at 0x0000017EB6723D30>), (<class 'int'>, <function html_int at 0x0000017EB6723A60>)])
print(htmlize.dispatch(int))
print(htmlize(100))

@htmlize.register(float)
def html_real(a):
    return f'{round(a, 2):.2f}'


@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/\n')

@htmlize.register(tuple)
@htmlize.register(list)
def html_list(l):
    items = [f'<li>{htmlize(item)}</li>' for item in l]
    return f'<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(dict)
def html_dict(d):
    items = [f'<li>{htmlize(k)}={htmlize(v)}</li>'
             for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlize.registry)
# dict_keys([<class 'object'>, <class 'int'>, <class 'float'>,
# <class 'str'>, <class 'list'>, <class 'tuple'>, <class 'dict'>])
print(htmlize((1, 2, 3)))
print(htmlize("""this
is a multi line string with
a < 10"""))