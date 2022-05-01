import os.path as op
import warnings
from functools import wraps

from flask import Blueprint, current_app, render_template, abort, g, url_for
from _compat import with_metaclass, as_unicode
import helpers as h



def expose(url='/', methods=('GET',)):
    def wrap(f):
        if not hasattr(f, '_urls'):
            f._urls = []
        f._urls.append((url, methods))
        return f
    return wrap


def expose_plugview(url='/'):
    def wrap(v):
        handler = expose(url, v.methods)

        if hasattr(v, 'as_view'):
            return handler(v.as_view(v.__name__))
        else:
            return handler(v)
    return wrap

# Base views
def _wrap_view(f):
    # Avoid wrapping view method twice
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
        return self._run_view(f, *args, **kwargs)
    inner._wrapped = True
    return inner


#######################################
#---<AdminViewMeta &  BaseViewClass---#
#######################################

class AdminViewMeta(type):

    def __init__(cls, classname, bases, fields):
        type.__init__(cls, classname, bases, fields)
        # Gather exposed views
        cls._urls = []
        cls._default_view = None
        for p in dir(cls):
            attr = getattr(cls, p)
            if hasattr(attr, '_urls'):
                # Collect methods
                for url, methods in attr._urls:
                    cls._urls.append((url, p, methods))
                    if url == '/':
                        cls._default_view = p
                # Wrap views
                setattr(cls, p, _wrap_view(attr))

class BaseViewClass(object):
    pass

###################
#---<BaseView >---#
###################

class BaseView(with_metaclass(AdminViewMeta, BaseViewClass)):
 
    @property
    def _template_args(self):
        args = getattr(g, '_admin_template_args', None)

        if args is None:
            args = g._admin_template_args = dict()

        return args

    def __init__(self, name=None, category=None, endpoint=None, url=None,
                static_folder=None, static_url_path=None,
                menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
   
        self.name = name
        self.category = category
        self.endpoint = self._get_endpoint(endpoint)
        self.url = url
        self.static_folder = static_folder
        self.static_url_path = static_url_path
        self.menu = None

        self.menu_class_name = menu_class_name
        self.menu_icon_type = menu_icon_type
        self.menu_icon_value = menu_icon_value

        # Initialized from create_blueprint
        self.admin = None
        self.blueprint = None

        # Default view
        if self._default_view is None:
            raise Exception(u'Attempted to instantiate admin view %s without default view' % self.__class__.__name__)

    def _get_endpoint(self, endpoint):
     
        if endpoint:
            return endpoint

        return self.__class__.__name__.lower()

    def _get_view_url(self, admin, url):
        """
            Generate URL for the view. Override to change default behavior.
        """
        if url is None:
            if admin.url != '/':
                url = '%s/%s' % (admin.url, self.endpoint)
            else:
                if self == admin.index_view:
                    url = '/'
                else:
                    url = '/%s' % self.endpoint
        else:
            if not url.startswith('/'):
                url = '%s/%s' % (admin.url, url)

        return url

    def create_blueprint(self, admin):
        """
            Create Flask blueprint.
        """
        # Store admin instance
        self.admin = admin

        # If the static_url_path is not provided, use the admin's
        if not self.static_url_path:
            self.static_url_path = admin.static_url_path

        # Generate URL
        self.url = self._get_view_url(admin, self.url)

        # If we're working from the root of the site, set prefix to None
        if self.url == '/':
            self.url = None
            # prevent admin static files from conflicting with flask static files
            if not self.static_url_path:
                self.static_folder = 'static'
                self.static_url_path = '/static/admin'

        # If name is not provided, use capitalized endpoint name
        if self.name is None:
            self.name = self._prettify_class_name(self.__class__.__name__)

        # Create blueprint and register rules
        self.blueprint = Blueprint(self.endpoint, __name__,
                                   url_prefix=self.url,
                                   subdomain=self.admin.subdomain,
                                   template_folder=op.join('templates', self.admin.template_mode),
                                   static_folder=self.static_folder,
                                   static_url_path=self.static_url_path)

        for url, name, methods in self._urls:
            self.blueprint.add_url_rule(url,
                                        name,
                                        getattr(self, name),
                                        methods=methods)

        return self.blueprint

    def render(self, template, **kwargs):
        """
            Render template

            :param template:
                Template path to render
            :param kwargs:
                Template arguments
        """
        # Store self as admin_view
        kwargs['admin_view'] = self
        kwargs['admin_base_template'] = self.admin.base_template

        # Provide i18n support even if flask-babel is not installed
        # or enabled.
        kwargs['_gettext'] = babel.gettext
        kwargs['_ngettext'] = babel.ngettext
        kwargs['h'] = h

        # Expose get_url helper
        kwargs['get_url'] = self.get_url

        # Expose config info
        kwargs['config'] = current_app.config

        # Contribute extra arguments
        kwargs.update(self._template_args)

        return render_template(template, **kwargs)

    def _prettify_class_name(self, name):
        """
            Split words in PascalCase string into separate words.

            :param name:
                String to prettify
        """
        return h.prettify_class_name(name)

    def is_visible(self):
        """
            Override this method if you want dynamically hide or show administrative views
            from Flask-Admin menu structure

            By default, item is visible in menu.

            Please note that item should be both visible and accessible to be displayed in menu.
        """
        return True

    def is_accessible(self):
        """
            Override this method to add permission checks.

            Flask-Admin does not make any assumptions about the authentication system used in your application, so it is
            up to you to implement it.

            By default, it will allow access for everyone.
        """
        return True

    def _handle_view(self, name, **kwargs):
        """
            This method will be executed before calling any view method.

            It will execute the ``inaccessible_callback`` if the view is not
            accessible.

            :param name:
                View function name
            :param kwargs:
                View function arguments
        """
        if not self.is_accessible():
            return self.inaccessible_callback(name, **kwargs)

    def _run_view(self, fn, *args, **kwargs):
        """
            This method will run actual view function.

            While it is similar to _handle_view, can be used to change
            arguments that are passed to the view.

            :param fn:
                View function
            :param kwargs:
                Arguments
        """
        return fn(self, *args, **kwargs)

    def inaccessible_callback(self, name, **kwargs):
        """
            Handle the response to inaccessible views.

            By default, it throw HTTP 403 error. Override this method to
            customize the behaviour.
        """
        return abort(403)

    def get_url(self, endpoint, **kwargs):
        """
            Generate URL for the endpoint. If you want to customize URL generation
            logic (persist some query string argument, for example), this is
            right place to do it.

            :param endpoint:
                Flask endpoint name
            :param kwargs:
                Arguments for `url_for`
        """
        return url_for(endpoint, **kwargs)

    @property
    def _debug(self):
        if not self.admin or not self.admin.app:
            return False

        return self.admin.app.debug



#####################
#---<FLASK ADMIN>---#
#####################
class Admin(object):
   
    def __init__(self, app=None, name=None,
                url=None, subdomain=None,
                index_view=None,
                translations_path=None,
                endpoint=None,
                static_url_path=None,
                base_template=None,
                template_mode=None,
                category_icon_classes=None):

        self.app = app

        self.translations_path = translations_path
        # Appends _views with Func add_view
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
        self.base_template = base_template or 'admin/base.html'
        self.category_icon_classes = category_icon_classes or dict()

        # Add index view
        self._set_admin_index_view(index_view=index_view, endpoint=endpoint, url=url)

        # Register with application
        if app is not None:
            self._init_extension()

    def add_view(self, view):
     
        # Add to views
        self._views.append(view)

        # If app was provided in constructor, register view with Flask app
        if self.app is not None:
            self.app.register_blueprint(view.create_blueprint(self))

        self._add_view_to_menu(view)

    def _set_admin_index_view(self, index_view=None,
                              endpoint=None, url=None):
        
        self.index_view = index_view or AdminIndexView(endpoint=endpoint, url=url)
        self.endpoint = endpoint or self.index_view.endpoint
        self.url = url or self.index_view.url

        print('==='*30)
        print(index_view)
        print(self.endpoint)
        print(self.url)
        print(self._views)
        print('==='*30)

        # Add predefined index view
        # assume index view is always the first element of views.
        if len(self._views) > 0:
            self._views[0] = self.index_view
            self._menu[0] = MenuView(self.index_view.name, self.index_view)
        else:
            self.add_view(self.index_view)

    def add_views(self, *args):
        for view in args:
            self.add_view(view)

    def add_sub_category(self, name, parent_name):

        name_text = as_unicode(name)
        parent_name_text = as_unicode(parent_name)
        category = self.get_category_menu_item(name_text)
        parent = self.get_category_menu_item(parent_name_text)
        if category is None and parent is not None:
            category = SubMenuCategory(name)
            self._menu_categories[name_text] = category
            parent.add_child(category)

    def add_link(self, link):
    
        if link.category:
            self.add_menu_item(link, link.category)
        else:
            self._menu_links.append(link)


    def add_menu_item(self, menu_item, target_category=None):
    
        if target_category:
            cat_text = as_unicode(target_category)

            category = self._menu_categories.get(cat_text)

            # create a new menu category if one does not exist already
            if category is None:
                category = MenuCategory(target_category)
                category.class_name = self.category_icon_classes.get(cat_text)
                self._menu_categories[cat_text] = category

                self._menu.append(category)

            category.add_child(menu_item)
        else:
            self._menu.append(menu_item)

    def _add_menu_item(self, menu_item, target_category):
        warnings.warn('Admin._add_menu_item is obsolete - use Admin.add_menu_item instead.')
        return self.add_menu_item(menu_item, target_category)

    def _add_view_to_menu(self, view):
        """
            Add a view to the menu tree

            :param view:
                View to add
        """
        self.add_menu_item(MenuView(view.name, view), view.category)

    def get_category_menu_item(self, name):
        return self._menu_categories.get(name)

    def init_app(self, app, index_view=None,
                 endpoint=None, url=None):
        """
            Register all views with the Flask application.

            :param app:
                Flask application instance
        """
        self.app = app

        self._init_extension()

        # Register Index view
        if index_view is not None:
            self._set_admin_index_view(
                index_view=index_view,
                endpoint=endpoint,
                url=url
            )

        # Register views
        for view in self._views:
            app.register_blueprint(view.create_blueprint(self))

    def _init_extension(self):
        if not hasattr(self.app, 'extensions'):
            self.app.extensions = dict()

        admins = self.app.extensions.get('admin', [])

        for p in admins:
            if p.endpoint == self.endpoint:
                raise Exception(u'Cannot have two Admin() instances with same'
                                u' endpoint name.')

            if p.url == self.url and p.subdomain == self.subdomain:
                raise Exception(u'Cannot assign two Admin() instances with same'
                                u' URL and subdomain to the same application.')

        admins.append(self)
        self.app.extensions['admin'] = admins

    def menu(self):
        """
            Return the menu hierarchy.
        """
        return self._menu

    def menu_links(self):
        """
            Return menu links.
        """
        return self._menu_links