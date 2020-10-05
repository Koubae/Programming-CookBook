

# Views without Decorators
from flask import Flask
app = Flask(__name__)


def index():
    pass


def user(username):
    pass

# Add a module that sets up an application which maps the functions to URLs:
from flask import Flask
from yourapplication import views
app = Flask(__name__)
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/user/<username>', view_func=views.user)