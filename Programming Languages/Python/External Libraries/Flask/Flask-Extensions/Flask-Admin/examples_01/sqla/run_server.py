from admin import app
from admin.data import build_sample_db
import os
import os.path as op

basedir = op.join(op.abspath(op.dirname(__file__)), 'admin')
database_path = op.join(basedir, app.config['DATABASE_FILE'])

if not os.path.exists(database_path):
    build_sample_db()


if __name__ == '__main__':
    app.run(debug=True)