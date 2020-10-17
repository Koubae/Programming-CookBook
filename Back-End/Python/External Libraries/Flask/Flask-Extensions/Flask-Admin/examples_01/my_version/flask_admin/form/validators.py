#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
top_dir = os.path.dirname(parent_dir)
sys.path.insert(0, parent_dir)

from wtforms.validators import StopValidation


class FieldListInputRequired(object):

    field_flags = ('required',)

    def __call__(self, form, field):
        if len(field.entries) == 0:
            field.errors[:] = []
            raise StopValidation('This field requires at least one item.')