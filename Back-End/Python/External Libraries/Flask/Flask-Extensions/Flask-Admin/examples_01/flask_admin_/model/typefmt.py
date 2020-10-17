import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import json
from jinja2 import Markup
from _compat import text_type

try:
    from enum import Enum
except ImportError:
    Enum = None


def null_formatter(view, value):
    return Markup('<i>NULL</i>')


def empty_formatter(view, value):
    return ''

def bool_formatter(view, value):

    glyph = 'ok-circle' if value else 'minus-sign'
    fa = 'check-circle' if value else 'circle-o'
    return Markup('<span class="fa fa-%s glyphicon glyphicon-%s icon-%s"></span>' % (fa, glyph, glyph))


def list_formatter(view, values):
    return u', '.join(text_type(v) for v in values)


def enum_formatter(view, value):
    return value.name

def dict_formatter(view, value):
    return json.dumps(value, ensure_ascii=False)


BASE_FORMATTERS = {
    type(None): empty_formatter,
    bool: bool_formatter,
    list: list_formatter,
    dict: dict_formatter
}

EXPORT_FORMATTERS = {
    type(None): empty_formatter,
    list: list_formatter,
    dict: dict_formatter
}

DETAIL_FORMATTERS = {
    type(None): empty_formatter,
    list: list_formatter,
    dict: dict_formatter
}

if Enum is not None:
    BASE_FORMATTERS[Enum] = enum_formatter
    EXPORT_FORMATTERS[Enum] = enum_formatter
    DETAIL_FORMATTERS[Enum] = enum_formatter

