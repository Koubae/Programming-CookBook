import sqlite3


# HACK:
basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db') 



conn = sqlite3.connect('tax_vat.db')

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS country_vat')
c.execute("""CREATE TABLE country_vat(
          country text,
          vat_rate real,
          threshold real)""")

conn.commit()

conn.close()


# ============================ < Simple Connection > ============================ #

import sqlite3
from sqlite3 import Error
import os


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sm_app.db')
connection = create_connection(path)


# ============================ < Flask Simple Connection > ============================ #

from flask import g
import sqlite3
import os

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'food_log.db' )

def connect_db():
    sql = sqlite3.connect(basedir)
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if  not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db




# ============================ < Simple Execute function > ============================ #

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# ============================ < Simple Table > ============================ #

# FAQ: Create User Table
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""

execute_query(connection, create_users_table)

# FAQ: Create Post Table with Foreign Key
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""
execute_query(connection, create_posts_table)

# FAQ: Create Comments Table with 2 Foreign Keys
create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL,  
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

# FAQ: Create Likes table with 2 Foreign Keys
create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

execute_query(connection, create_comments_table)
execute_query(connection, create_likes_table)


# ============================ < Flask Better Connection > ============================ #
# NOTE: schema_2.sql

# create table [table_name] (
#     ...
# );

# ....

# NOTE: database.py


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
  
# NOTE: app.py

from flask import Flask
from database import get_db, check_db
import os
from database import get_db, check_db


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Init DB -from database.py
init_db = check_db(app)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()