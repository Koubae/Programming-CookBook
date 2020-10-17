import os


SECRET_KEY = os.urandom(16)

FLASK_ADMIN_SWATCH = 'cerulean'

# Create in-memory database
DATABASE_FILE = 'database.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False