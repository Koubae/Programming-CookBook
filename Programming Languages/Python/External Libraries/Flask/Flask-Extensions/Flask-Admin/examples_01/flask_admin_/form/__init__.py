#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, current_dir)

from wtforms import form, __version__ as wtforms_version
from wtforms.fields.core import UnboundField

from fields import *
from widgets import *
from upload import *


class BaseForm(form.Form):
    try:
        _translations = Translations()
    except:
        print('Not translations yet')
    
    def __init__(self, formdata=None, obj=None, prefix=u'', **kwargs):
        self.obj = obj
        super(BaseForm, self).__init__(formdata=formdata, obj=obj, prefix=prefix, **kwargs)
    
    # Not Implemented
    def _get_translations(self):
        pass


class FormOpts(object):

    __slots__ = ['widget_args', 'form_rules']

    def __init__(self, widget_args=None, form_rules=None):
        self.widget_args = widget_args or {}
        self.form_rules = form_rules

def recreate_field(unbound):

    if not isinstance(unbound, UnboundField):
        raise ValueError('recreate_field expects UnboundField instance, %s was passed.' % type(unbound))
    return unbound.field_class(*unbound.args, **unbound.kwargs)

if int(wtforms_version[0]) > 1:
    from os import urandom
    from flask import session, current_app
    from wtforms.csrf.session import SessionCSRF
    from _compat import text_type

    class SecureForm(BaseForm):

        class Meta:
            csrf = True
            csrf_class = SessionCSRF
            _csrf_secret = urandom(24)

            @property
            def csrf_secret(self):
                secret = current_app.secret_key or self._csrf_secret
                if isinstance(secret, text_type):
                    secret = secret.encode('utf-8')
                return secret
            
            @property
            def csrf_context(self):
                return session

else:
    class SecureForm(BaseForm):
        def __init__(self, *args, **kwargs):
            raise Exception("SecureForm requires WTForms 2+")
                



