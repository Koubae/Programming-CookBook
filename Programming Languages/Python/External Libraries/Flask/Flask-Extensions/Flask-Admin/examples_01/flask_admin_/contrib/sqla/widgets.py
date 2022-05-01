#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
top_dir = os.path.dirname(parent_dir)
sys.path.insert(0, top_dir)

from wtforms.widgets.core import escape
from _backwards import Markup

class CheckBoxListInput:

    template = (
        '<div class="checkbox">'
            ' <label>'
                '  <input id="%(id)s" name="%(name)s" value="%(id)s" '
                'type="checkbox"%(selected)s>%(label)s'
            ' </label>'
        '</div>'
    )

    def __call__(self, field, **kwargs):

        items = []

        for val, label, selected, in field.iter_choicers():
            args = {
                'id': val,
                'name': field.name,
                'label': escape(label),
                'selected': 'checked' if selected else '',
            }
            items.append(self.template % args)
        return Markup('',join(items))
        