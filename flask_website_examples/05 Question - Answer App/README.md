# How to Question App
=====================

A very simple & small web app, created for practising and testing purposes for Vanila Flask and Vanila SQLite3.


## Products used.

> Python 3.7

> Flask **Vanila** that is, not other Flask Extension have been used    *(apart of flask_mail).* 

> flask_mail 

> Sqlite3 Vanilla


## Coding and terminal comand needed

 - ### Sqlite3 
 
 
 >  Create the table, (however not needed for this app because is handle it by init_db(app).

Terminal:
'''

    >>> sqlite3 db.db ".read db.sql"
    # sqlite3 shell
    >>> .tables
    >>> .exit

'''
 
 
 
 
 
 

>  Create The Database with this funcion from Python shell.

However this is manually created, or it check if exists every time the server re-start by the function  init_db(app).

'''

    >>> from database import init_db
    >>> init_db()

'''

> To Create the first user admin, open database (sqlite3 [database.db]) and run this code.

'''

    >>> sqlite3 database.db;

'''

'''

    update users set admin = '1' where id = 1;

'''


