import sqlite3
from flask import g
import os 


DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__), 'database.db'))

def get_db():

    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    
    return db


@app.teardown_appcontext
def close_connection(exception):

    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
    

@app.route('/')
def index():
    cur = get_db().cursor()
    # ...


# with app.app_context():
#     # now you can use get_db()

# Initial Schemas

def init_db():

    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# >>> from yourapplication import init_db
# >>> init_db()

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        print('==='*15)
        print('>>> Creating Database... ---> Database Created!')
        init_db()
        print('==='*15)
    app.run(debug=True)

##########################################
#--------------< VARIATION>--------------#
##########################################


basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'food_log.db' )

def connect_db():
    sql = sqlite3.connect(basedir)
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if  not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db