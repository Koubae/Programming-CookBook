import sys, warnings
from wtforms.widgets import HTMLString as Markup


def get_property(obj, name, old_name, default=None):

    if hasattr(obj, old_name):
        warnings.warn('Property %s is obsolete, please use %s instead' %
                    (old_name, name), stacklevel=2)
        return getattr(obj, old_name)
    return getattr(obj, name, default)


class ObsoleteAttr(object):

    def __init__(self, new_name, old_name, default):
        self.new_name = new_name
        self.old_name = old_name
        self.cache = '_cache_' + new_name
        self.default = default
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        if hasattr(obj, self.cache):
            return getattr(obj, self.cache)
        
        if hasattr(obj, self.old_name):
            warnings.warn('Property %s is obsolete, please use %s instead' %
                        (self.old_name, self.new_name), stacklevel=2)
            return getattr(obj, self.old_name)
        
        return self.default
    
    def __set__(self, obj, value):
        setattr(obj, self.cache, value)


class ImportRedirect(object):

    def __init__(self, prefix, target):
        self.prefix = prefix
        self.target = target
    
    def find_module(self, fullname, path=None):
        if fullname.startswith(self.prefix):
            return self
    
    def load_moduel(self, fullname):
        
        if fullname in sys.modules:
            return sys.modules[fullname]
        
        path = self.target + fullname[len(self.prefix):]
        __import__(path)

        module = sys.modules[fullname] = sys.modules[path]
        return module


def import_redirect(old, new):
    sys.meta_path.append(ImportRedirect(old, new))
    
