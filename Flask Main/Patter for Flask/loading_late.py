
from werkzeug.utils import import_string, cached_property

class LazyView(object):

    def __init__(self, import_name):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        return self.view(*args, **kwargs)


# You can define your central place to combine the views like this:

from flask import Flask
from yourapplication.helpers import LazyView

app = Flask(__name__)
app.add_url_rule('/',
                view_func=LazyView('yourapplication.views.index'))
app.add_url_rule('/user/<username>',
                view_func=LazyView('yourapplication.views.user'))


# Further optimize


def url(import_name, url_rules=[], **options):
    view = LazyView('yourapplication.' + import_name)
    for url_rule in url_rules:
        app.add_url_rule(url_rule, view_func=view, **options)

# add a single route to the index view
url('views.index', ['/'])

# add two routes to a single function endpoint
url_rules = ['/user/','/user/<username>']
url('views.user', url_rules)