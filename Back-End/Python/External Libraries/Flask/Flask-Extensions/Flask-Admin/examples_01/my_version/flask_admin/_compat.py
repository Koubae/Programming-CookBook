import sys
# Various tools
from functools import reduce
from urllib.parse import urljoin, urlparse, quote
from collections import OrderedDict



text_type = str
string_types = (str, )
integer_types = (int, )

iter_keys = lambda d: iter(d.keys())
itervalues = lambda d: iter(d.values())
iteritems = lambda d: iter(d.items())
filter_list = lambda f, l: list(filter(f, l))

# Decode From Bytes => Str
def as_unicode(s):
    if isinstance(s, bytes):
        return s.decode('utf-8')
    return str(s)

def csv_encode(s):
    ''' Returns unicode string expected by Python 3's csv module '''
    return as_unicode(s)


def with_metaclass(meta, *bases):

    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__

        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)
    return metaclass('temporary_class', None, {})

    