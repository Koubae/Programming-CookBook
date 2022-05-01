# Flask-Admin -Full Project Break Down
=============================


#### Taken from [Flask-Admin Docs](#https://github.com/flask-admin/flask-admin/tree/master/flask_admin)


Repository that breaks down the meain components of Flask-admin with the purpose of learn how it works and understand what it does behind the scene.


## flask_admin/helpers.py

- set_current_view(view): Set the current view object to Flask g


>flask.g:

A namespace object that can store data during an application context. This is an instance of Flask.app_ctx_globals_class, which defaults to ctx._AppCtxGlobals.

This is a good place to store resources during a request. During testing, you can use the Faking Resources and Context pattern to pre-configure such resources.

app_ctx_globals_class
alias of flask.ctx._AppCtxGlobals

#### class flask.ctx._AppCtxGlobals[DOCS](#https://flask.palletsprojects.com/en/1.1.x/api/#flask.ctx._AppCtxGlobals)

A plain object. Used as a namespace for storing data during an application context.

Creating an app context automatically creates this object, which is made available as the g proxy.


-----------------------

```

- is_required_form_field(field): imports from form/validators.py ---> FieldListInputRequired(object):

from wtforms.validators import StopValidation

class StopValidation(Exception):
    """
    Causes the validation chain to stop.

    If StopValidation is raised, no more validators in the validation chain are
    called. If raised with a message, the message will be added to the errors
    list.
    """
    def __init__(self, message='', *args, **kwargs):
        Exception.__init__(self, message, *args, **kwargs)

```

- **def is_safe_url(target):**  Prevent urls like "\\www.google.com", some browser will change \\ to // (eg: Chrome)[STACK OVERFLOW](#https://stackoverflow.com/questions/10438008)


- **def resolve_ctx(context):** uses Jinja decorator @contextfunction, jinja2\utils.py:


```

def contextfunction(f):
    """This decorator can be used to mark a function or method context callable.
    A context callable is passed the active :class:`Context` as first argument when
    called from the template.  This is useful if a function wants to get access
    to the context or functions provided on the context object.  For example
    a function that returns a sorted list of template variables the current
    template exports could look like this::

        @contextfunction
        def get_exported_names(context):
            return sorted(context.exported_vars)
    """
    f.contextfunction = True
    return f

```


-----------------------


## flask_admin/menu.py


-  BaseMenu(object): is the class top level. All other classes inherit from it.

```

def add_child(self, menu):
        # TODO: Check if menu item is already assigned to some parent
        menu.parent = self
        self._children.append(menu)

```
Appends children class to parent class


-----------------------


# flask_admin/base.py
-----------------------

> class AdminViewMeta(type):


- etattr(cls, p, _wrap_view(attr))  

-----------------------

> _template_args['']

These arguments are local for this request and will be discarded
in the next request.

Any value passed through ``_template_args`` will override whatever
parent view function passed to the template.

**FUNCTION**

```

@property
    def _template_args(self):

        args = getattr(g, '_admin_template_args', None)

        if args is None:
            args = g._admin_template_args = dict()
        return args

```

To note that the portion of '_admin' it can be given in the updated class as *self._template_args['form'] = form*

For example::

```

class MyAdmin(ModelView):
    @expose('/')
    def index(self):
        self._template_args['name'] = 'foobar'
        self._template_args['code'] = '12345'
        super(MyAdmin, self).index()


```

#### OR Taken from [Flask-Admin Docs](#https://github.com/flask-admin/flask-admin/blob/master/examples/auth-flask-login/app.py)

```


class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        
        return super(MyAdminIndexView, self).index()

    # Login
    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        
        form = LoginForm(request.form)
        #------------------------------------
        x = form.validate_login
        print(x)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)
    
        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') +'">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        
        return super(MyAdminIndexView, self).index()
        #------------------------------------
    # Sign Up
    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
      
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
       
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

```
-----------------------

> ### class AdminViewMeta(type):

```

for p in dir(cls):
    attr = getattr(cls, p)

            
```
> Extracts all attributs from Class AdminViewMeta for then assign it to the Variable attr:

- __class__
- __delattr__
- __dict__   
- __dir__
- __doc__
- __eq__
- __format__
- __ge__
- __getattribute__
- __gt__
- __hash__
- __init__
- __init_subclass__
- __le__
- __lt__
- __module__
- __ne__
- __new__
- __reduce__
- __reduce_ex__
- __repr__
- __setattr__
- __sizeof__
- __str__
- __subclasshook__
- __weakref__
- _default_view
- _get_endpoint
- _template_args
- _urls


-----------------------

> ### BaseView(with_metaclass(AdminViewMeta, BaseViewClass)):

```
def __init__(self, name=None, category=None, endpoint=None, url=None,
                static_folder=None, static_url_path=None,
                menu_class_name=None, menu_icon_type=None, menu_icon_value=None)

:param menu_icon_type:
            Optional icon. Possible icon types:

                - `flask_admin.consts.ICON_TYPE_GLYPH` - Bootstrap glyph icon
                - `flask_admin.consts.ICON_TYPE_FONT_AWESOME` - Font Awesome icon
                - `flask_admin.consts.ICON_TYPE_IMAGE` - Image relative to Flask static directory
                - `flask_admin.consts.ICON_TYPE_IMAGE_URL` - Image with full URL
        :param menu_icon_value:
            Icon glyph name or URL, depending on `menu_icon_type` setting

```

>  def is_visible(self):  ===> Choose is the View is visivle in the Menu structure, it has to be is_accessible
> def is_accessible(self): ===> By default, it will allow access for everyone.

> def _handle_view(self, name, **kwargs): ==>   This method will be executed before calling any view method.

It will execute the ``inaccessible_callback`` if the view is not accessible.

> _run_view(self, fn, *args, **kwargs): ==>  This method will run actual view function.

>   def inaccessible_callback(self, name, **kwargs): ==>  Handle the response to inaccessible views,  By default, it throw HTTP 403 error

-----------------------

> ### class AdminIndexView(BaseView):  

##### Default administrative interface index page when visiting the ``/admin/`` URL.


It can be overridden by passing your own view class to the ``Admin`` constructor:

```

admin = Admin(index_view=MyHomeView())

```
 Also, you can change the root url from /admin to / with the following:


```

admin = Admin(app, index_view=AdminIndexView(
                    name='Home',
                    template='admin/myhome.html',
                    url='/'
                )
            )

```
Default values for the index page are:

* If a name is not provided, 'Home' will be used.
* If an endpoint is not provided, will default to ``admin``
* Default URL route is ``/admin``.
* Automatically associates with static folder.
* Default template is ``admin/index.html``

-----------------------

> def add_views(self, *args):

Add one or more views to the collection.

Examples:

```

    admin.add_views(view1)
    admin.add_views(view1, view2, view3, view4)
    admin.add_views(*my_list)

```

> def init_app(self, app, index_view(None), endpoint=None, url=None):

Is quite important function:

1 It triggers the _init_extension(self) Admin Class method, 
2 It register the index view to Admin class method ==> _set_admin_index_view
3 It register the views with Flask function .register_blueprint


> Extracts all attributs from Class Admin for then assign it to the Variable attr:


- __class__
- __delattr__
- __dict__
- __dir__
- __doc__
- __eq__
- __format__
- __ge__
- __getattribute__
- __gt__
- __hash__
- __init__
- __init_subclass__
- __le__
- __lt__
- __module__
- __ne__
- __new__
- __reduce__
- __reduce_ex__
- __repr__
- __setattr__
- __sizeof__
- __str__
- __subclasshook__
- __weakref__
- _add_menu_item
- _add_view_to_menu
- _init_extension
- _menu
- _menu_categories
- _menu_links
- _set_admin_index_view
- _views
- add_link
- add_links
- add_menu_item
- add_sub_category
- add_view
- add_views
- app
- base_templase
- category_icon_classes
- endpoint
- get_category_menu_item
- index_view
- init_app
- menu
- menu_linkst
- name
- static_url_path
- subdomain
- template_mode
- translations_path
- url

---------------------------

- app
- translations_path
- _views
- _menu
- _menu_categories
- _menu_links
- name
- index_view
- endpoint
- url
- static_url_path
- subdomain
- base_templase
- template_mode
- category_icon_classes

-------------------- 


>_views if is > 0 it becomes 'self.index_view' which by default it'll set as AdminIndexView(endpoint=endpoint, url=url).

So to get the <__main__.AdminIndexView object> user admin._views[0]. 

To get a AdminIndexView attribue ==> admin._views[0].attr example admin._views[0].endpoint

-------------------------------------------


## flask_admin/__init__.py


> def recreate_field(unbound): => Very interesting Function approach

```

Create new instance of the unbound field, resetting wtforms creation counter.

:param unbound:
UnboundField instance

```
-------------------------------------------

> class SecureForm(BaseForm):

```
BaseForm with CSRF token generation and validation support.
Requires WTForms 2+

```


## flask_admin/rules.py


> class BaseRule(object): 

```
 Base form rule. All form formatting rules should derive from `BaseRule`.


```


> def visible_fields(self): => I don't understand what it does?


```

@property
    def visible_fields(self):
        return []
```

> class NestedRule(BaseRule):


```
Nested rule. Can contain child rules and render them.

```


> class Text(BaseRule):


```
Render text (or HTML snippet) from string.

```

> class HTML(Text):

```

Shortcut for `Text` rule with `escape` set to `False`.

```

> class Macro(BaseRule):

```

 Render macro by its name from current Jinja2 context.

```

> class Container(Macro):


```

Render container around child rule.

```