from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, current_user, login_required
from flask_security.forms import RegisterForm
from wtforms import StringField, TextAreaField
from flask_wtf import FlaskForm 
from datetime import datetime
import os

app = Flask(__name__)

app.config['DATABASE_FILE'] = 'database.db'
base_dir = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), 
            app.config['DATABASE_FILE']
            )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + base_dir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(16)
app.config['DEBUG'] = True
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = 'somesaltfortheforum'
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ==============================#
# ---- < DATABASE MODELS > ---- #
# ==============================#

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(250))


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    replies = db.relationship('Reply', backref='user', lazy='dynamic')


class Thread(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(200))
    date_created = db.Column(db.DateTime())

    replies = db.relationship('Reply', backref='thread', lazy='dynamic')

    def last_post_date(self):
        last_reply = Reply.query.filter_by(thread_id=self.id).order_by(Reply.id.desc()).first()

        if last_reply:
            return last_reply.date_created

        return self.date_created


class Reply(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(200))
    date_created = db.Column(db.DateTime())


# ========================#
# ---- < FORMS WTF > ---- #
# ========================#


class ExtendRegisterForm(RegisterForm):

    name = StringField('Name')
    username = StringField('Username')


class NewThread(FlaskForm):

    title = StringField('Title')
    description = StringField('Description')


class NewReply(FlaskForm):

    message = TextAreaField('Message')

# ======================#
# ---- < CONFIGS > ---- #
# ======================#

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=ExtendRegisterForm)


# ====================#
# ---- < VIEWS > ---- #
# ====================#

# Index
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():

    form = NewThread()

    if form.validate_on_submit():
        new_thread = Thread(title=form.title.data, description=form.description.data, date_created=datetime.now())
        db.session.add(new_thread)
        db.session.commit()

    threads = Thread.query.all()

    return render_template('index.html', form=form, threads=threads, current_user=current_user)

# Profile
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)

# Thred
@app.route('/thread/<thread_id>', methods=['GET', 'POST'])
def thread(thread_id):

    form = NewReply()

    thread = Thread.query.get(int(thread_id))

    if form.validate_on_submit():
        reply = Reply(user_id=current_user.id, message=form.message.data, date_created=datetime.now())
        thread.replies.append(reply)
        db.session.commit()

    replies = Reply.query.filter_by(thread_id=thread_id).all()

    return render_template('thread.html', thread=thread, form=form, replies=replies, current_user=current_user)


if __name__ == '__main__':
    if not os.path.exists(base_dir):
        print('==='*15)
        print('>>> Creating Database... ---> Database Created!')
        db.create_all()
        print('==='*15)
    app.run(debug=True)
   
