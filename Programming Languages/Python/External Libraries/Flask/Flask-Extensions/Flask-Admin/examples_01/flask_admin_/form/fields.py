#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import time 
import datetime
import json

from wtforms import fields
from _compat import text_type, as_unicode

# from widgets import * as admin_widgets
import form.widgets as admin_widgets


__all__ = ['DateTimeField', 'TimeField', 'Select2Field', 'Select2TagsField', 'JSONField']


class DateTimeField(fields.DateTimeField):

    widget = admin_widgets.DateTimePickerWidget()

    def __init__(self, label=None, validators=None, format=None, **kwargs): #  :param format:Format for text to date conversion. Defaults to '%Y-%m-%d %H:%M:%S'
        super(DateTimeField, self).__init__(label, validators, **kwargs)
        self.format = format or '%Y-%m-%d %H:%M:%S'


class TimeField(fields.Field):

    widget = admin_widgets.TimePickerWidget()

    def __init__(self, label=None, validators=None, formats=None, 
                default_format=None, widget_format=None, **kwargs): # :param default_format: Default time format. Defaults to '%H:%M:%S'
        super(TimeField, self).__init__(label, validators, **kwargs)
        self.formats = formats or ('%H:%M:%S', '%H:%M',
                                    '%I:%M:%S%p', '%I:%M%p',
                                    '%I:%M:%S %p', '%I:%M %p')
        self.default_format = default_format or '%H:%M:%S'
    
    def _value(self):
        if self.raw_data:
            return u' '.join(self.raw_data)
        elif self.data is not None:
            return self.data.strftime(self.default_format)
        else:
            return u''
    
    def process_formdata(self, valuelist):
        if valuelist:
            date_str = u' '.join(valuelist)

            if date_str.strip():
                for format in self.formats:
                    try:
                        timetuple = time.strptime(date_str, format)
                        self.data = datetime.time(timetuple.tm_hour,
                                                timetuple.tm_min,
                                                timetuple.tm_sec)
                        return
                    except ValueError:
                        pass
                raise ValueError(gettext('Invalid Time format.'))
            else:
                self.data = None
                

class Select2Field(fields.SelectField):

    widget = admin_widgets.Select2Widget()

    def __init__(self, label=None, validators=None, coerce=text_type,
                choices=None, allow_blank=False, blank_text=None, **kwargs):
        super(Select2Field, self).__init__(label, validators, coerce, choices, **kwargs)
        self.allow_blank = allow_blank
        self.blank_text = blank_text or ' '

    def iter_choices(self):
        if self.allow_blank:
            yield (u'__None', self.blank_text, self.data is None)
        
        for value, label, in self.choices:
            yield (value, label, self.coerce(value) == self.data)
    
    def process_data(self, value):
        if values is None:
            self.data = None
        else:
            try:
                self.data = self.coerce(value)
            except (ValueError, TypeError):
                self.data = None
    
    def process_formdata(self, valuelist):
        if valuelist:
            if valuelist[0] == '__None':
                self.data = None
            else:
                try:
                    self.data = self.coerce(valuelist[0])
                except ValueError:
                    raise ValueError(self.gettext(u'Invalid Choice: could not coerce.'))
    
    def pre_validate(self, form):
        if self.allow_blank and self.data is None:
            return
        super(Select2Field, self).pre_validate(form)
    

class Select2TagsField(fields.StringField):

    widget = admin_widgets.Select2TagsWidget()

    def __init__(self, label=None, validators=None, save_as_list=False, coerce=text_type, **kwargs):
        self.save_as_list = save_as_list
        self.coerce = coerce
        super(Select2TagsField, self).__init__(label, validators, **kwargs)
    
    def process_formdata(self,valuelist):
        if valuelist:
            if self.save_as_list:
                self.data = [self.coerce(v.strip()) for v in valuelist[0].split(',') if v.strip()]
            else:
                self.data = self.coerce(valuelist[0])
    
    def _value(self):
        if isinstance(self.data, (list, tuple)):
            return u','.join(as_unicode(v) for v in self.data)
        elif self.data:
            return as_unicode(self.data)
        else:
            return u''


class JSONField(fields.TextAreaField):

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            # prevent utf8 characters from being converted to ascii
            return as_unicode(json.dumps(self.data, ensure_ascii=False))
        else:
            return ''
    
    def process_formdata(self, valuelist):

        if valuelist:
            value = valuelist[0]
            if not valie:
                self.data = None
                return
            try:
                self.data = json.loads(valuelist[0])
            except ValueError:
                raise ValueError(self.gettext('Invalid JSON'))