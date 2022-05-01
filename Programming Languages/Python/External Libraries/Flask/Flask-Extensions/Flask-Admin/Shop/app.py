from werkzeug.security import generate_password_hash

from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
# Flask Admin
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from os.path import dirname, join, abspath
from os import urandom
from flask_login import LoginManager, login_user, logout_user, current_user, UserMixin



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

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(50))
    age = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.id)
class UserView(ModelView):

    column_exclude_list = []
    column_display_pk = True
    can_edit = True
    can_delete = True
    can_export = True

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password, method='sha256')

        inline_models = [Comment]
    
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return '<h1> You are Logged in</h1>'


class CommentView(ModelView):
    
    create_modal = True


class NotificationsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/notification.html')


# Add views to Admin

admin.add_view(UserView(User, db.session))
admin.add_view(CommentView(Comment, db.session))
admin.add_view(FileAdmin(path, '/uploads/', name='Uploads'))
admin.add_view(NotificationsView(name='Notifications', endpoint='notify'))



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


@app.route('/')
def home():
    return redirect(url_for('admin.index'))

@app.route('/hola')
def hola():
    return render_template('other.html')

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




if __name__ == '__main__':
    app.run(debug=True)