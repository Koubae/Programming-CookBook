#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from flask import json
from jinja2 import escape 
from wtforms.widgets import html_params
from wtforms.widgets import HTMLString as Markup

from _compat import as_unicode, text_type
from helpers import get_url
from form.widgets import RenderTemplateWidget


class InlineFieldListWidget(RenderTemplateWidget):
    
    def __init__(self):
        super(InlineFieldListWidget, self).__init__('admin/model/inline_field_list.html')

class InlineFormWidget(RenderTemplateWidget):

    def __init__(self):
        super(InlineFormWidget, self).__init__('admin/model/inline_form.html')

    def __call__(self, field, **kwargs):
        kwargs.setdefault('form_opts', getattr(field, 'form_opts', None))
        return super(InlineFormWidget, self).__call__(field, **kwargs)


class AjaxSelect2Widget(object):

    def __init__(self, multiple=False):
        self.multiple = multiple
    
    def __call__(self, field, **kwargs):
        kwargs.setdefault('data-role', 'select2-ajax')
        kwargs.setdefault('data-url', get_url('.ajax_lookup', name=field.loader.name))

        allow_blank = getattr(field, 'allow_blank', False)
        if allow_blank and not self.multiple:
            kwargs['data-allow-blank'] = u'1'
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', 'hidden')

        if self.multiple:
            result = []
            ids = []

            for value in field.data:
                data = field.loader.format(value)
                result.append(data)
                ids.append(as_unicode(data[0]))
            separator = getattr(field, 'separator', ',')
            kwargs['value'] = separator.join(ids)
            kwargs['data-json'] = json.dumps(result)
            kwargs['data-multiple'] = u'1'
        else:
            data = field.loader.format(field.data)

            if data:
                kwargs['value'] = data[0]
                kwargs['data-json'] = json.dumps(data)
        placeholder = field.loader.options.get('placeholder', 'Please select Model')
        kwargs.setdefault('data-placeholder', placeholder)
        minimum_input_length = int(field.loader.options.get('minimum_input_length', 1))
        kwargs.setdefault('data-minimum-input-length', minimum_input_length)

        return Markup('<input %S>' % html_params(name=field.name,) **kwargs)
    

class XEditableWidget(object):

    def __call__(self, field, **kwargs):
        display_value = kwargs.pop('dispay_value', '')
        kwargs.setdefault('data-value', display_value)
        kwargs.setdefault('data-role', 'x-editable')
        kwargs.setdefault('data-url', './ajax/update/')
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        kwargs.setdefault('href', '#')
        
        if not kwargs.get('pk'):
            raise Exception('pk required')
        kwargs['data-pk'] = str(kwargs.pop('pk')) 
        kwargs['data-csrf'] = kwargs.pop('csrf', '')
        kwargs = self.get_kwargs(field, kwargs)

        return Markup( 
            '<a %a>%s</a>'% (html_params(**kwrgs),
                            escape(display_value))
        ) 

        def get_kwargs(self, field, kwargs):

            if field.type == 'StringField':
                kwargs['data-type'] == 'text'
            elif field.type == 'TextAreaField':
                kwargs['data-type'] = 'textarea'
                kwargs['data-rows'] = '5'
            elif field.type == 'BooleanField':
                kwargs['data-type'] = 'select2'
                kwargs['data-value'] = '1' if field.data else '' 
                kwargs['data-source'] = json.dumps([
                    {'value': '', 'text': 'No'},
                    {'value': '1', 'text': 'Yes'}
                ]) 
                kwargs['data-role'] = 'x-editable-boolean' 
            elif field.type in['Select2Field', 'SelectField']:
                kwargs['data-type'] = 'select2'
                choices = [{'value': x, 'text': y} for x, y in field.choices]
                if getattr(field, 'allow_blank', False):
                    choices.insert(0, {'value': '__None', 'text': ''})
                kwargs['data-source'] = json.dumps(choices)
            elif field.type == 'DataField':
                kwargs['data-type'] = 'combodate'
                kwargs['data-format'] = 'YYYY-MM-DD'
                kwargs['data-template'] = 'YYYY-MM-DD'
            elif field.type == 'DateTimeField':
                kwargs['data-type'] = 'combodate'
                kwargs['data-format'] = 'YYYY-MM-DD HH:mm:ss'
                kwargs['data-template'] = 'YYYY-MM-DD  HH:mm:ss'
                # x-editable-combodate uses 1 minute increments
                kwargs['data-role'] = 'x-editable-combodate'
            elif field.type == 'TimeField':
                kwargs['data-type'] = 'combodate'
                kwargs['data-format'] = 'HH:mm:ss'
                kwargs['data-template'] = 'HH:mm:ss'
                kwargs['data-role'] = 'x-editable-combodate'
            elif field.type == 'IntegerField':
                kwargs['data-type'] = 'number'
            elif field.type in ['FloatField', 'DecimalField']:
                kwargs['data-type'] = 'number'
                kwargs['data-step'] = 'any'
            elif field.type in ['QuerySelectField', 'ModelSelectField',
                            'QuerySelectMultipleField', 'KeyPropertyField']:
                kwargs['data-type'] = 'select2'
                choices = []
                selected_ids = []
                for value, label, selected in field.iter_choices():
                    try:
                        label = text_type(label)
                    except TypeError:
                        label = ''
                    choices.append({'value': text_type(value), 'text': label})
                    if selected:
                        selected_ids.append(value)
                kwargs['data-source'] = json.dumps(choices)

                if field.type == 'QuerySelectMultipleField':
                    kwargs['data-role'] = 'x-editable-select2-multiple'
                    separator =getattr(field, 'separator', ',')
                    kwargs['data-value'] = separator.join(selected_ids)
                else:
                    kwargs['data-value'] = text_type(selected_ids[0])
            else:
                raise Exception('Unsupported field type: %s' % (type(field), ))
            return kwargs