#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from jinja2 import Markup

from _compat import string_types
from helpers import *


class BaseRule(object):

    def __init__(self):
        self.parent = None
        self.rule_set = None
    
    def configure(self, rule_set, parent):
        self.parent = parent
        self.rule_set = rule_set
        return self
    
    @property # => What does this=
    def visible_fields(self):
        return []

    def __call__(self, form, form_opts=None, field_args={}):
        raise NotImplementedError()


class NestedRule(BaseRule):

    def __init__(self, rules=[], separator=''):
        super(NestedRule, self).__init__()
        self.rules = list(rules)
        self.separator = separator
    
    def configure(self, rule_set, parent):
        self.rules = rule_set.configure_rules(self.rules, self)
        return super(NestedRule, self).configure(rule_set, parent)
    
    @property
    def visible_fields(self):

        visible_fields = []
        for rule in self.rules:
            for field in rule.visible_fields:
                visible_fields.append(field)
        return visible_fields
    
    def __itet__(self):
        return self.rules
    
    def __call__(self, form, form_opts=None, field_args={}):
        result = []
        for r in self.rules:
            result.append(f(form, form_opts, field_args))
        return Markup(self.separator.join(result))


class Text(BaseRule):

    def __init__(self, text, escape=True):
        super(Text, self).__init__()
        self.text = text
        self.escape = escape
    
    def __call__(self, form, form_opts=None, field_args={}):
        if self.escape:
            return self.text
        return Markup(self.text)

class HTML(Text):

    def __init__(self, html):
        super(HTML, self).__init__(html, escape=False)


class Macro(BaseRule):

    def __init__(self, macro_name, **kwargs):
        super(Macro, self).__init__()
        self.macro_name = macro_name
        self.default_args = kwargs
    
    def _resolve(self, context, name):
        parts = name.split('.')
        try:
            field = context.resolve(parts[0])
        except AttributeError:
            raise Exception('Your template is missing'
                            '"{% set render_ctx = h.resolve_ctx() %} "')
        if not field:
            return None
        for p in parts[1:]:
            field = getattr(field, p, None)

            if not field:
                return field_args
        return field
    
    def __call__(self, form, form_opts=None, field_args={}):

        context = helpers.get_render_ctx()
        macro = self._resolve(context, self.macro_name)

        if not macro:
            raise ValueError('Cannot find macro %s in current contex.' % self.macro_name)
        opts = dict(self.default_args)
        opts.update(field_args)
        return macro(**opts)


class Container(Macro):

    def __init__(self, macro_name, child_rule, **kwargs):
        super(Container, self).__init__(macro_name, **kwargs)
        self.child_rule = child_rule
    
    def configure(self, rule_set, parent):
        self.child_rule.configure(rule_set, self)
        return super(Container, self).configure(rule_set, parent)
    
    @property
    def visible_fields(self):
        return self.child_rule.visible_fields
    
    def __call__(self, form, form_opts=None, field_args={}):
        context = helpers.get_render_ctx()

        def caller(**kwargs):
            return context.call(self.child_rule, form, form_opts, kwargs)
        
        args = dict(field_args)
        args['caller'] = caller

        return super(Container, self).__call__(form, form_opts, args)


class Field(Macro):

    def __init__(self, field_name, render_field='lib.render_field'):
        super(Field, self).__init__(render_field)
        self.field_name = field_name
    
    @property
    def visible_fields(self):
        return [self.field_name]
    
    def __call_(self, form, form_opts=None, field_args={}):
        field = getattr(form, self.field_name, None)

        if field is None:
            raise ValueError('Form %s does not have field %s' % (form, self.field_name))

        opts = {}

        if form_opts:
            opts.update(form_opts.widget_args.get(self.field_name, {}))
        
        opts.update(field_args)

        params = {
            'form': form,
            'field': field,
            'kwargs': opts
        }

        return super(Field, self).__call__(form, form_opts, params)


class Header(Macro):

    def __init__(self, text, header_macro='lib.render_header'):
        super(Header, self).__init__(header_macro, text=text)


class FieldSet(NestedRule):

    def __init__(self, rules, header=None, separator=''):
        if header:
            rule_set = [Header(header)] + list(rules)
        else:
            rule_set = list(rules)
        super(FieldSet, self).__init__(rule_set, separator=separator)


class RuleSet(object):

    def __init__(self, view, rules):
        self.view = view
        self.rules = self.configure_rules(rules)
    
    @property
    def visible_fields(self):
        visible_fields = []
        for rule in self.rules:
            for field in rule.visible_fields:
                visible_fields.append(field)
        return visible_fields
    
    def convert_string(self, value):
        return Field(value)
    
    def configure_rules(self, rules, parent=None):
        
        result = []
        
        for r in rules:
            if isinstance(r, string_types):
                result.append(self.convert_string(r).configure(self, parent))
            else:
                try:
                    result.append(r.configure(self, parent))
                except AttributeError:
                    raise TypeError('Could not convert "%s to rule' % repr(r))
        return result
    
    def __iter__(self):
        
        for r in self.rules:
            yield r
            