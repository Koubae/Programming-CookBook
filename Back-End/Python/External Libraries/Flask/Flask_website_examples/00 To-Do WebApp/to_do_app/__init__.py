from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
import os   


app = Flask(__name__)

basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite')

app.config.update( 
    SECRET_KEY= b'0>\xcbvE4\xd2\xd1\x81=y\xe2\xf2O\x19(',
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SQLALCHEMY_DATABASE_URI = basedir
)

db = SQLAlchemy(app)


# Core Blueprint
from to_do_app.core.views import core 
app.register_blueprint(core)

# Tag Blueprint
from to_do_app.tag.views import tag_bp
app.register_blueprint(tag_bp)

# Reminder Blueprint
from to_do_app.reminder.views import reminder
app.register_blueprint(reminder)
