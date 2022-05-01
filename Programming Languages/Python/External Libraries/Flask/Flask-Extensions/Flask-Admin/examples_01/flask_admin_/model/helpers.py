
#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

def prettify_name(name):
    return name.replace('_', ' ').title()


def get_mdict_item_or_list(mdict, key):

    if hasattr(mdict, 'getlist'):
        v = mdict.getlist(key)
        if len(v) == 1:
            value = v[0]
            if value == '':
                value = None
            return value
        elif len(v) == 0:
            return None
        else:
            return tuple(v)
    return None

    