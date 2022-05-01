import sqlite3
import os

path_ = os.path
db_name = 'main.db'
basedir = path_.join(path_.abspath(path_.dirname(__file__)), db_name)
db_ = dict()


def connect_db():
    sql = sqlite3.connect(basedir)
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(db_, 'database_conn'):
        db_['database_conn'] = connect_db()
    return db_['database_conn']


def execute(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except sqlite3.Error as err:
        print(f'Failed to commit to database, error = {err}')


def execute_many(conn, query):
    cursor = conn.cursor()
    try:
        cursor.executemany(query)
        conn.commit()
    except sqlite3.Error as err:
        print(f'Failed to commit to database, error = {err}')


def execute_script(conn, script):
    cursor = conn.cursor()
    try:
        with open(script, 'r') as s:
            cursor.executescript(s.read())
            conn.commit()
    except sqlite3.Error as err:
        print(f'Failed to commit to database, error = {err}')


def fetch(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchone()
    except sqlite3.Error as err:
        print(f'Failed to fetch data from database, error = {err}')


def fetch_all(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as err:
        print(f'Failed to fetch data from database, error = {err}')


def init_db(query=None, script=None):
    if not path_.isfile(basedir):
        get_db()
    if query or script:
        conn = get_db()
        if query:
            execute(conn, query)
        elif script:
            execute_script(conn, script)


def check_tables():
    conn = get_db()
    get_tables = "SELECT name FROM sqlite_master WHERE (TYPE = 'table') AND (name NOT LIKE 'sqlite_%')"
    tables = [list(table)[0] for table in fetch_all(conn, get_tables)]
    return tables


def back_up():
    conn = get_db()
    sql_backup = sqlite3.connect(basedir.replace('main', 'backup'))
    sql_backup.row_factory = sqlite3.Row

    def progress(status, remaining, total):
        print(f'Copied {total - remaining} of {total} pages | Status = {status}')

    try:
        with sql_backup:
            conn.backup(sql_backup, pages=3, progress=progress)
    except sqlite3.Error as error:
        print("Error while taking backup: ", error)
    finally:
        if sql_backup:
            sql_backup.close()
            conn.close()


def resest_and_vacuum_db(backup=False):
    conn = get_db()
    reset_db = "select 'drop table ' || name || ';' from sqlite_master where type = 'table'"
    _vacuum = "VACUUM;"
    check = "PRAGMA INTEGRITY_CHECK;"
    if backup:
        back_up()
    reset_query = fetch_all(get_db(), reset_db)
    for query in reset_query:
        execute(conn, query[0])
    execute(conn, _vacuum)
    database_state = list(fetch(conn, check))
    print(f'Databased has been Reset and vacuumed, Integrity check result = {database_state}')

    # HACK: """
    #  PRAGMA writable_schema = 1;
    #  DELETE FROM sqlite_master WHERE TYPE IN ('table', 'index', 'trigger');
    #  PRAGMA writable_schema = 0;
    #  VACUUM;