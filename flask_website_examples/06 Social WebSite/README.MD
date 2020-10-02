# Social Blog Wep ite
=================================

A simple social blog web site



Requirements:

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Sqlite3](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask-Script](https://flask-script.readthedocs.io/en/latest/)
- [Flask-Uploads](https://pythonhosted.org/Flask-Uploads/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)

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


--------------------------------------------------------------------------------------------


## Flask-Script
================

*from flask_script import Manager, Server*

```

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())

```

>>> **python app.py runserver**

==========================================

##### NOTE

issue with Flask Uploads:

https://stackoverflow.com/questions/60192172/importerror-cannot-import-name-filestorage-from-werkzeug

--------------------------------------------------------------------------------------------

##### NOTE TODO

Understand Front end imlementation



--------------------------------------------------------------------------------------------


