#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import os.path as op
import warnings

from functools import wraps 

from flask import Blueprint, current_app, render_template, abort, g, url_for, Flask
# from flask_admin import babel
from _compat import with_metaclass, as_unicode
import helpers as h

# For compatibility reasons import MenuLink
from menu import MenuCategory, MenuView, MenuLink, SubMenuCategory 


def expose(url='/', methods=('GET',)):
    
    def wrap(f):
        if not hasattr(f, '_urls'):
            f._urls = []
        f._urls.append((url, methods))
        return f
    return wrap



def expose_plugview(url='/'):
    """
        Decorator to expose Flask's pluggable view classes
        (``flask.views.View`` or ``flask.views.MethodView``).
    """
    def wrap(v):
        handler = expose(url, v.methods)

        if hasattr(v, 'as_view'):
            return handler(v.as_view(v.__name__))
        else:
            return handler(v)
    return wrap

# Base views
def _wrap_view(f):
    #Avoid wrapping view methods twice
    if hasattr(f, '_wrapped'):
        return f
    @wraps(f)
    def inner(self, *args, **kwargs):
        # Store current admin view
        h.set_current_view(self)

        # Check if administrative piece is accessible
        abort = self._handle_view(f.__name__, **kwargs)
        if abort is not None:
            return abort
        return self.run_view(f, *args, **kwargs)
    
    inner._wrapped = True

    return inner

class AdminViewMeta(type):
    """
        View metaclass.

        Does some precalculations (like getting list of view methods from the class) to avoid
        calculating them for each view class instance.
    """
    def __init__(cls, classname, bases, fields):
        type.__init__(cls, classname, bases, fields)

        # Gather exsoped Views
        cls._urls = []
        cls._default_view = None

        for p in dir(cls):
            attr = getattr(cls, p)
            if hasattr(attr, '_urls'):
                # Collect Methods
                for url, methods in attr._urls:
                    cls._urls.append((url, p, methods))
            
                    if url == '/':
                        cls._default_view = p
                setattr(cls, p, _wrap_view(attr))
           


class BaseViewClass(object):
    pass

####################
#---< BaseView >---#
####################
class BaseView(with_metaclass(AdminViewMeta, BaseViewClass)):

    @property
    def _template_args(self):
        # Pass Value through "_template_args['form'] = form"
        # Overrides the parent view function passed to the template
        args = getattr(g, '_admin_template_args', None)
        # Note 
        if args is None:
            args = g._admin_template_args = dict()
        return args

    def __init__(self, name=None, category=None, endpoint=None, url=None, 
                static_folder=None, static_url_path=None, 
                menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        self.name = name
        self.category = category
        self.endpoint = self._get_endpoint(endpoint) # Function defined --> Line 123 
        self.url = url
        self.static_folder = static_folder
        self.static_url_path = static_url_path
        self.menu = None
        self.menu_class_name = menu_class_name
        self.menu_icon_type = menu_icon_type
        self.menu_icon_value = menu_icon_value

        # Initialized from create_blueprint ---> Line 151 
        self.admin = None
        self.blueprint = None

        # Default View
        # if self._default_view is None:
        #     raise Exception(u'Attempted to instantiate admin view %s without default view' % self.__class__.__name__)

    def _get_endpoint(self, endpoint):
        """
            Generate Flask endpoint name. By default converts class name to lower case if endpoint is
            not explicitly provided.
        """
        if endpoint:
            return endpoint
        return self.__class__.__name__.lower()

    
    def _get_view_url(self, admin, url):
        """
            Generate URL for the view. Override to change default behavior.
        """
        if url is None:
            if admin.url != '/':
                url ='%S/%S' % (admin.url, self.endpoint)
            else:
                if self == admin.index_view:
                    url = '/'
                else:
                    url = '/%s' % self.endpoint
        else:
            if not url.startswith('/'):
                url = '%s/%s' & (admin.url, url)
        return url

    def create_blueprint(self, admin):

        self.admin = admin

        # If the static_url_path is not provided, use the admin's
        if not self.static_url_path:
            self.static_url_parh = admin.static_url_path
        
        # Generate URL
        self.url = self._get_view_url(admin, self.url)  # FUnction at ----> Line 134

        if self.url == '/':
            self.url = None
            # Prevent admin's static file conflicting with Flask's
            if not self.static_url_path:
                self.static_folder = 'static'
                self.static_url_path = '/static/admin'
        
        # If name is not provided, use capitalized endpoint name
        if self.name is None:
            self.name = self._prettify_class_name(self.__class__.__name__) # Function defined --> Below 
        
        # Create a Blueprint and register rules
        self.blueprint = Blueprint(self.endpoint, __name__, 
                                    url_prefix=self.url,
                                    subdomain=self.admin.subdomain,
                                    template_folder=op.join('templates', self.admin.template_mode), # TODO --> How it does this
                                    static_folder=self.static_folder,
                                    static_url_path=self.static_url_path)

        for url, name, methods in self._urls:
            self.blueprint.add_url_rule(url, name, getattr(self, name), methods=methods)
        
        return self.blueprint
    

    def render(self, template, **kwargs):

        # Store self as admin_view
        kwargs['admin_view'] = self
        kwargs['admin_base_template'] = self.admin.base_template

        kwargs['_gettext'] = None   # TODO, will it break <---- ???
        kwargs['_ngettext'] = None
        kwargs['h'] = h

        # Expose get_url_helper
        kwargs['get_url'] = self.get_url

        # Exppose config info
        kwargs['config'] = current_app.config

        # Extra agrs
        kwargs.update(self._template_args)
        
        return render_template(template, **kwargs)

    def _prettify_class_name(self, name): # TODO ---> How does this function work?

        return h.prettify_class_name(name)
    
    # View Function 
    #################################################################################
    def is_visible(self):
        return True
    
    def is_accessible(self):
        return True
    
    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return self.inaccessible_callback(name, **kwargs) # Function below

    def _run_view(self, fn, *args, **kwargs):
        return fn(self, *args, **kwargs)
    
    def inaccessible_callback(self, name, **kwargs):
        return abort(403)
    
    def get_url(self, endpoint, **kwargs):
        return url_for(endpoint, **kwargs)
    
    @property
    def _debug(self):
        if not self.admin or not self.admin.app:
            return False
        return self.admin.app.debug


#########################
#---<AdminIndexView >---#
#########################
class AdminIndexView(BaseView):

    def __init__(self, name=None, category=None, endpoint=None,
                url=None, template='admin/index.html', menu_class_name=None,
                menu_icon_type=None, menu_icon_value=None):
        super(AdminIndexView, self).__init__(name, category, endpoint or 'admin', '/admin' if url is None else url,  '/static',
                                            menu_class_name=menu_class_name, menu_icon_type=menu_icon_type, menu_icon_value=menu_icon_value)
        self._template = template
    
    @expose()
    def index(self):
        return self.render(self._template)

#################
#---< Admin >---#
#################
class Admin(object):
    
    def __init__(self, app=None, name=None, url=None, subdomain=None, index_view=None,
                translations_path=None, endpoint=None, static_url_path=None,
                base_template=None, template_mode=None, category_icon_classes=None):
        self.app = app
        self.translations_path = translations_path
        
        self._views = []
        self._menu = []
        self._menu_categories = dict()
        self._menu_links = []

        if name is None:
            name = 'Admin'
        self.name = name
        self.index_view = index_view or AdminIndexView(endpoint=endpoint, url=url)
        self.endpoint = endpoint or self.index_view.endpoint
        self.url = url or self.index_view.url
        self.static_url_path = static_url_path
        self.subdomain = subdomain
        self.base_templase = base_template or 'admin/base.html'
        self.template_mode = template_mode or 'bootstrap2'
        self.category_icon_classes = category_icon_classes or dict()

        # Add Index Viex
        self._set_admin_index_view(index_view=index_view, endpoint=endpoint, url=url) # Function defined Below

        # Register with application
        if app is not None:
            self._init_extension() # Function defined Below
    
    # Add Views
    #################################################################################
    def add_view(self, view):

        # Add to Views
        self._views.append(view)
        # If app was provided in constructor, register view with Flask App
        if self.app is not None:
            self.app.register_blueprint(view.create_blueprint(self))
        
        self._add_view_to_menu(view)
    
    def add_views(self, *args):
        for view in args:
            self.add_view(view)
    
    def _set_admin_index_view(self, index_view=None, endpoint=None, url=None):
        """
            Add the admin index view.
        """
        self.index_view = index_view or AdminIndexView(endpoint=endpoint, url=url)
        self.endpoint = endpoint or self.index_view.endpoint
        self.url = url or self.index_view.url

        if len(self._views) > 0:
            self._views[0] = self.index_view
            self._menu[0] = MenuView(self.index_view.name, self.index_view)
        else:
            self.add_view(self.index_view)

    def add_sub_category(self, name, parent_name):

        name_text = as_unicode(name)
        parent_name_text = as_unicode(parent_name) # Function defined _compat.py
        category = self.get_category_menu_item(name_text)#  Function defined below
        parent = self.get_category_menu_item(parent_name_text)
        if category is None and parent is not None: # Checks if is a Parent or Child Category
            category = SubMenuCategory(name)
            self._menu_categories[name_text] = category
            parent.add_child(category)
    
    def add_link(self, link):
        """
            Add link to menu links collection.
        """
        if link.category:
            self.add_menu_item(link, link.category)
        else:
            self._menu_links.append(link)
    
    def add_links(self, *args):
        for link in args:
            self.add_link(link)
    # Add Menu
    #################################################################################
    def add_menu_item(self, menu_item, target_category=None):

        if target_category:
            cat_text = as_unicode(target_category)
            category = self._menu_categories.get(cat_text)
            # Create a new Menu category (if doesn't alredy exist)
            if category is None:
                category = MenuCategory(target_category)
                category.class_name = self.category_icon_classes.get(cat_text)
                self._menu_categories[cat_text] = category
                self._menu.append(category)
            category.add_child(menu_item)
        else:
            self._menu.append(menu_item)
    
    def _add_menu_item(self, menu_item, target_category): # TODO ==> Check what this does and then delete it
        warnings.warn('Admin._add_menu_item is obsolete use Admin.add_menu_item instead')
        return self.add_menu_item(menu_item, target_category)
    
    def _add_view_to_menu(self, view):
        self.add_menu_item(MenuView(view.name, view), view.category)
    
    def get_category_menu_item(self, name):
        return self._menu_categories.get(name)

    # Initialize
    #################################################################################
    def init_app(self, app, index_view=None, endpoint=None, url=None):
        """
            Register all views with the Flask application.
        """
        self.app = app
        self._init_extension() # Function defined below

        # Register Index View
        if index_view is not None:
            self._set_admin_index_view(index_view=index_view, endpoint=endpoint, url=url)
        
        # Register View
        for view in self._views:
            app.register_blueprint(view.create_blueprint(self))

    def _init_extension(self):
        if not hasattr(self.app, 'extensions'):
            self.app.extensions = dict()
        
        admins = self.app.extensions.get('admin', [])

        for p in admins:
            if p.endpoint == self.endpoint:
                raise Exception(u'Cannot hace two Admin instances with the same' u'endpoint name')
            
            if p.url == self.url and p.subdomain == self.subdomain:
                raise Exception(u'Cannot assign two Admin() instances with same' u' URL and subdomain to the same app')
        
        admins.append(self)
        self.app.extensions['admin'] = admins

    def menu(self):
        return self._add_menu_item
    
    def menu_linkst(self):
        return self._menu_links

    
# app = Flask(__name__)

# admin = Admin(app)
# admin_2 = Admin(app, name='Hii')
#attr = getattr(cls, p)

# # for i in admin.__dict__:
# #     print(i)
# #     print('- - -'*10)
# #     print(getattr(admin, i))
# #     print('==='*30)

# for i in admin._views[0].__dict__:
#     print(i)
#     print('- -  -'*10)
#     print(getattr(admin._views[0], i))
#     print('==='*30)







