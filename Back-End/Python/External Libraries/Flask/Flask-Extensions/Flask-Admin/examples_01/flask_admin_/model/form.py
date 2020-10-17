#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect, warnings
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


from form import BaseForm, rules
from _compat import iteritems

from wtforms.fields import HiddenField
from wtforms.fields.core import UnboundField
from wtforms.validators import InputRequired
from model.widgets import XEditableWidget


def convers(*args):
    def _inner(func):
        func._converter_for = frozenset(args)
        return func
    return _inner

def create_editable_list_form(form_base_class, form_class, widget=None):

    if widget is None:
        widget = XEditableWidget()

    class ListForm(form_base_class):
        list_form_pk = HiddenField(validators=[InputRequired()])
    for name, obj in iteritems(form_class.__dict__):
        obj.kwargs['widget'] = widget
        setattr(ListFor, name, obj)

        if name == 'list_form_pk':
            raise Exception('Form already has a list_form_pk column.')
    
    return ListForm


class InlineBaseFormAdmin(object):

    _defaults = ['form_base_class', 'form_columns', 'form_excluded_columns', 'form_args', 'form_extra_fields']

    def __init__(self, **kwargs):
        for k in self._defaults:
            if not hasattr(self, k):
                setattr(self, k, None)

        for k, v in iteritems(kwargs):
            setattr(self, k, v)
        
        form_rules = getattr(self, 'form_rules', None)

        if form_rules:
            self._form_rules = rules.RuleSet(self, form_rules)
        else:
            self._form_rules = None
    
    def get_form(self):
        return None

    def postprocess_form(self, form_class):
        return form_class
    
    def on_model_change(self, form, model, is_created):
        pass

    def _on_model_change(self, form, model, is_created):

        try:
            self.on_model_change(form, mode, is_created)
        except TypeError:
            msg = ('%s.on_model_change() now accepts third ' +
                'parameter is_created. Please update your code') % self.model
            warnings.warn(msg)

            self.on_model_change(form, model)


class InlineFormAdmin(InlineBaseFormAdmin):

    def __init__(self, mode, **kwargs):
        self.model = model
        super(InlineFormAdmin, self).__init__(**kwargs)


class ModelConverterBase(object):


    def __init__(self, converters=None, use_mro=True):
        self.use_mro = use_mro
        if not converters:
            converters = {}
        for name in dir(self):
            obj = getattr(self, name)
            if hasattr(obj, '_converter_for'):
                for classname in obj._converter_for:
                    converters[classname] = obj
        self.convers = converters
    
    def get_converter(self, column):
        if self.use_mro:
            types = inspect.getmro(type(column.type))
        else:
            types = [type(column.type)]
        for col_type in types:
            type_string = '%s.%s' % (col_type.__module__, col_type.__name__)

            if type_string in self.converters:
                return self.converster[type_string]
        
        for col_type in types:
            if col_type.__name__ in self.converters:
                return self.converters[col_type.__name__]

        return None
    
    def get_form(self, model, base_class=BaseForm,
                only=None, exclude=None,
                field_args=None):
        raise NotImplementedError()


class InlineModelConverterBase(object):

    form_admin_class = InlineFormAdmin

    def __init__(self, view):
        self.view = view

    def get_label(self, info, name):
        form_name = getattr(infor, 'form_label', None)
        if form_name:
            return form_name
        column_lebels = getattr(self.view, 'column_labels', None)

        if column_lebels and name in column_lebels:
            return column_lebels[name]
        return None
    
    def get_info(self, p):
        if isinstance(p, tuple):
            return self.form_admin_class(p[0], **p[1])
        elif isinstance(p, self.form_admin_class):
            return p
        return None


class FieldPlaceholder(object):

    def __init__(self, field):
        self.field = field
        
