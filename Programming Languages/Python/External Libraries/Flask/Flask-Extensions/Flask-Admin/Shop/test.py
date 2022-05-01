from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from flask_admin.contrib.fileadmin import FileAdmin
from os.path import dirname, join, abspath
from os import urandom
from flask_login import LoginManager, login_user, logout_user, current_user



app = Flask(__name__)

basedir = 'sqlite:///' + join(abspath(dirname(__file__)), 'data.sqlite')
my_secret = urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = basedir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = my_secret

db = SQLAlchemy(app)
admin = Admin(app, template_mode='bootstrap3')
login_manager = LoginManager(app)

path = join(dirname(__file__), 'uploads')

admin.add_view(UserView(User, db.session))
admin.add_view(CommentView(Comment, db.session))
admin.add_view(FileAdmin(path, '/uploads/', name='Uploads'))
admin.add_view(NotificationsView(name='Notifications', endpoint='notify'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


@app.route('/login')
def login():
    try:
        user = User.query.filter_by(id=1).first()
        login_user(user)
    except AttributeError as err:
        print(err)
        return redirect(url_for('admin.index'))

    return redirect(url_for('admin.index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.index'))


if __name__  == '__main__':
    app.run(debug=True)