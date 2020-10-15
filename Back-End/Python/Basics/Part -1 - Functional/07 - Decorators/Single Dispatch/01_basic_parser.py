from html import escape
from decimal import Decimal


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return f'{a}(<i>{str(hex(a))}</i>)'


def html_real(a):
    return f'{round(a, 2):.2f}'


def html_str(s):
    return html_escape(s).replace('/n', '<br/>\n')


def html_list(l):
    items = (f'<li>{html_escape(item)}</li>'
             for item in l)
    return f'<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = (f'<li>{html_escape(k)}={html_escape(v)}</li>'
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# print(html_str("""this is
# a multi line string
# with special characters: 10 < 100"""))
# this is
# a multi line string
# with special characters: 10 &lt; 100


def htmlize(arg):
    # INT
    if isinstance(arg, int):
        return html_int(arg)
    # FLOAT AND DECIMALS
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    # STR
    elif isinstance(arg, str):
        return html_str(arg)
    # LIST or TUPLE (Sequence)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    # DICT
    elif isinstance(arg, dict):
        return html_dict(arg)
    else: # default behavior - just html escape string representation
        return html_escape(str(arg))


print(htmlize([1, 2, 3]))
print(htmlize(dict(key1=1, key2=2)))
print(htmlize(255))

print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))


############################################
# Second Version

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'