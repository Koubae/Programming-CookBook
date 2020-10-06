import os
from flask_script import Manager, Server
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')

app.config['UPLOADED_PHOTOS_DEST'] = 'images'
app.config['SQLALCHEMY_DATABASE_URI'] = basedir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.urandom(16)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views import *
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())


if __name__ == '__main__':
    manager.run()