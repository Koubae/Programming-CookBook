from html import escape
from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence


@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def htmlize_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


print(htmlize.dispatch(int))

@htmlize.register(Sequence)
def html_sequence(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')

print(htmlize('abc'))

@htmlize.register(tuple)
def html_tuple(t):
    items = [escape(str(item)) for item in t]
    return '({0})'.format(', '.join(items))

print(htmlize(['a', 100, 3.14]))

# <ul>
# <li>a</li>
# <li>100(<i>0x64</i)</li>
# <li>3.14</li>
# </ul>

print(htmlize(('a', 100, 3.14)))

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(int)
def _(a):
    return '{0}({1})'.format(a, str(hex(a)))


@htmlize.register(str)
def _(s):
    return escape(s).replace('\n', '<br/>\n')


@htmlize.register(str)
def _(s):
    return escape(s).replace('\n', '<br/>\n')


htmlize.register(float)(lambda f: f'{f:.2f}')
