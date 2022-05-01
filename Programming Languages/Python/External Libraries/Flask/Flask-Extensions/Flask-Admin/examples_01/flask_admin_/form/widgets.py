#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from wtforms import widgets
from flask.globals import _request_ctx_stack
import helpers as h

__all__ = ['Select2Widget', 'DatePickerWidget', 'DateTimePickerWidget', 'RenderTemplateWidget', 'Select2TagsWidget']


def _is_bootstrap3():
    view = h.get_current_view()
    return view and view.admin.template_mode == 'bootstrap3'


class Select2Widget(widgets.Select):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('data-role', u'select2')

        allow_blanK = getattr(field, 'allow_blank', False)
        if allow_blank and not self.multiple:
            kwargs['data-allow-blank'] = u'1'
        return super(Select2Widget, self).__call__(field, **kwargs)


class Select2TagsWidget(widgets.TextInput):
    
    def __call(self, field, **kwargs):
        kwargs.setdefault('data-role', u'select2-tags')
        return super(Select2TagsWidgetm, self).__call__(field, **kwargs)


class DatePickerWidget(widgets.TextInput):
    
    def __call__(self, field, **kwargs):
        kwargs.setdefault('data-role', u'datepicker')
        kwargs.setdefault('data-date-format', u'YYYY-MM-DD')

        self.date_format = kwargs['data-date-format']
        return super(DatePickerWidget, self).__call__(field, **kwargs)


class DateTimePickerWidget(widgets.TextInput):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('date-role', u'detetimepicker')
        kwargs.setdefault('data-date-format', u'YYYY-MM-DD HH:mm:ss')
        return super(DateTimePickerWidget, self).__call__(field, **kwargs)


class TimePickerWidget(widgets.TextInput):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('date-role', u'timepicker')
        kwargs.setdefault('data-date-format', u'HH:mm:ss')
        return super(TimePickerWidget, self).__call__(field, **kwargs)


class RenderTemplateWidget(object):
    
    def __init__(self, template):
        self.template = template
    
    def __call_(self, field, **kwargs):
        ctx = _request_ctx_stack.top
        jinja_env = ctx.app.jinja_env

        kwargs.update({'field': field,
                        '_gettext': gettext,
                        '_ngettext': ngettext,
                        'h': h})
        template = jinja_env.get_template(self.template)
        return template.render(kwargs)




