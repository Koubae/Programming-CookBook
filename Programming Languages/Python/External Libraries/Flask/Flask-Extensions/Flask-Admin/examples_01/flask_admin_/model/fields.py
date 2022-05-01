#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect, warnings
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import itertools

from wtforms.validators import ValidationError
from wtforms.fields import FieldList, FormField, SelectFieldBase
from wtforms.fields import _unset_value as unset_value

from _compat import iteritems
from widgets import (InlineFieldListWidget, InlineFormWidget, AjaxSelect2Widget)


class InlineFieldList(FieldList):

    widget = InlineFieldListWidget()

    def __init__(self, *args, **kwargs):
        super(InlineFieldList, self).__init__(*args, **kwargs)
    
    def __call__(self, **kwargs):
        meta = getattr(self, 'meta', None)
        if meta:
            template = self.unbound_field.bind(form=None, name='', _meta=meta)
        else:
            template = self.unbound_field.bind(form=None, name='')
        if isinstance(template, FormField):
            template.separator = ''
        
        template.process(None)
        return self.widget(self,
                        template=template,
                        check=self.display_row_controls,
                        **kwargs)
    
    def display_row_controls(self, field):
        return True
    
    def process(self, formdata, data=unset_value):
        res = super(InlineFieldList, self).process(formdata, data)

        if formdata:
            for f in self.entries:
                key = 'del-%s' % f.id
                f._should_delete = key in formdata
        return res
    
    def validate(self, form, extra_validators=tuple()):
        self.errors = []

        for subfield in self.entries:
            if not self._should_delete(subfield) and not subfield.validate(form):
                self.errors.append(subfield.errors)
        chain = itertools.chain(self.validators, extra_validators)
        self._run_validation_chain(form, chain)
        
        return len(self.errors) == 0
    
    def should_delete(self, field):
        return getattr(field, '_should_delete', False)
    
    def populate_obj(self, obj, name):

        values = getattr(obj, name, None)
        try:
            ivalues = iter(values)
        except TypeError:
            ivalues = iter([])
        
        candidates = itertools.chain(ivalues, itertools.repeat(None))
        _fake = type(str('_fake'), (object, ), {})

        output = []
        for field, data in zip(self.entries, candidates):
            if not self.should_delete(field):
                fake_obj = _fake()
                fake_obj.data = data
                field.populate_obj(fake_obj, 'data')
                output.append(fake_obj.data)
        setattr(obj, name, output)


class InlineFormField(FormField):

    widget = InlineFormWidget()


class InlineModelFormField(FormField):

    widget = InlineFormWidget()

    def __init__(self, form_class, pk, form_opts=None, **kwargs):
        super(InlineModelFormField, self).__init__(form_class, **kwargs)

        self._pk = pk
        self.form_opts = form_opts
    
    def get_pk(self):
        
        if instance(self._pk, (tuple, list)):
            return tuple(getattr(self.form, pk).data for pk in self._pk)
        return getattr(self.form, self._pk).data
    
    def populate_obj(self, obj, name):
        for name, field in iteritems(self.form._fields):
            if name != self._pk:
                field.populate_obj(obj, name)


class AjaxSelectField(SelectFieldBase):

    widget = AjaxSelect2Widget()
    separator = ','

    def __init__(self, loader, label=None, validators=None, allow_blank=False, blank_test=u'', **kwargs):
        super(AjaxSelectField, self).__init__(label, validators, **kwargs)
        self.loader = loader
        self.allow_blank = allow_blank
        self.blank_text = blank_test
    
    def _get_data(self):
        if self._formdata:
            model = self.loader.get_one(self._formdata)
            if model is not None:
                self._set_data(model)
        return self._data
    
    def _set_data(self, data):
        self._data = data
        self._formdata = None

    data = property(_get_data, _set_data)

    def _format_item(self, item):
        value = self.loader.format(self.data)
        return (value[0], value[1], True)
    
    def process_formdata(self, valuelist):
        if valuelist:
            if self.allow_blank and valuelist[0] == u'__None':
                self.data = None
            else:
                self._data = None
                self._formdata = valuelist[0]
    
    def pre_validate(self, form):
        if not self.allow_blank and self.data is None:
            raise ValidationError(u'Not a valid choicee')


class AjaxSelectMultipleField(AjaxSelectField):

    widget = AjaxSelect2Widget(multiple=True)

    def __init__(self, loader, label=None, validators=None, dafault=None, **kwargs):
        if default is None:
            default = []
        super(AjaxSelectMultipleField, self).__init__(loader, label, validators, default=default, **kwargs)
        self._invalid_formdata = False
    
    def _get_data(self):
        formdate = self._formdata
        if formdata:
            data = []
            #TODO: Optimize?
            for item in formdata:
                model = self.loader.get_one(item) if item else None
                 
                if model:
                    data.append(model)
                else:
                    self._invalid_formdata = True
            self._set_data(data)
        return self._data
    
    def _set_data(self, data):
        self._data = data
        self._formdata = None
    
    data = property(_get_data, _set_data)

    def process_formdata(self, valuelist):
        self._formdata = set()

        for field in valuelist:
            for n in field.split(self.separator):
                self._formdata.add(n)
    
    def pre_validate(self, form):
        if self._invalid_formdata:
            raise ValidationError(u'Not a valid choice.')
