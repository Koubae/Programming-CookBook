# Forum Website
=================================

A simple Forum Web Site



Requirements:

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Sqlite3](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask-Security](https://pythonhosted.org/Flask-Security/)
- [email_validator](https://pypi.org/project/email-validator/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [bycrypt](https://pypi.org/project/bcrypt/)

--------------------------------------------------------------------------------------------


### Credits

This is a revisited project created by PrettyPrinted:

- [Pretty Printed- Udemy](https://www.udemy.com/course/the-ultimate-flask-course/)

- [Pretty Printed Website](https://prettyprinted.com/)

- [Pretty Printed Youtube Channel](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)

--------------------------------------------------------------------------------------------


## Flask-migrate
================

```

Terminal Commands

 1) CSM to env folder.
 2) Enter (optional): >>> set FLASK_APP=app.py   #or whatever name 
 3) >>> flask db init  #initiate the database
 4) >>> flask db migrate -m "first commit"
 5) flask db upgrade

 >>> Flask db init
 >>> flask db migrate -m "first commit"
 >>> flask db upgrade

 1)  

 >>> python app.py db init

 2 ) 

 >>> python app.py db migrate

3 ) 

>>> python app.py db upgrade

```

## Flask-SQLAlchemy
================


- Use of db.Table

- db.relationship use of 'secondary=' and 'backref=db.backref' 


## Flask-Security
================

- **SQLAlchemyUserDatastore(db, User, Role)**

A SQLAlchemy datastore implementation for Flask-Security that assumes 
the use of the Flask-SQLAlchemy extension.

==========================================

##### NOTE




--------------------------------------------------------------------------------------------
