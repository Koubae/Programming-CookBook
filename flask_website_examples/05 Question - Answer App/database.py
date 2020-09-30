from flask import g
import sqlite3
import os


app_db = 'forum.db'
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), app_db)

def f_sep():
    print('==='*30)

# Connect to Database
def connect_db():
    sql = sqlite3.connect(basedir)
    sql.row_factory = sqlite3.Row
    return sql

# Add DB Connection to G Object
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Initialize DB 
def init_db(app):
    '''
    Create The Database with this funcion from Python shell.
    >> from database import init_db
    >> init_db()
    '''
    
    with app.app_context():
        db = get_db()
        with app.open_resource('schema_2.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
   

# Check if DB exists
def check_db(app):
    if not os.path.isfile(basedir):
        f_sep()
        print('Creating Database with Sqlite3... Done!')
        init_db(app)
        f_sep()

