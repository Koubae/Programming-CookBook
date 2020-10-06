from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
import os


app = Flask(__name__)

basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
app.config['UPLOADED_PHOTOS_DEST'] = 'images' 
app.config['SQLALCHEMY_DATABASE_URI'] = basedir 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True 
app.config['SECRET_KEY'] = os.urandom(16)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views import *
from app_func import time_since

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()






