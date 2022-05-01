from os.path import dirname, join, abspath
from os import urandom
import os
from os.path import isfile
from flask import Flask, redirect, url_for, render_template, g

# Flask Admin
from flask_admin import Admin, BaseView, expose
from flask_admin.helpers import get_current_view, get_url
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink


from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

basedir = 'sqlite:///' + join(abspath(dirname(__file__)), 'data.sqlite')
my_secret = urandom(16)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = basedir 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = my_secret

db = SQLAlchemy(app)

def check_if_db_exists(db):
    database_file = basedir.split('sqlite:///')
    database_file = database_file[1]
   
    if not isfile(database_file):
        print('==='*30)
        db.create_all()
        print('Creating Database...Done!')
        print('==='*30)
    else:
        print('Database alreadY On')

admin = Admin(app, name='microblog', template_mode='bootstrap3')


########################
#-------<MODELS>-------#
########################

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(60))

    # Relationship
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    cars = db.relationship('Car', backref='user', lazy='dynamic')
    role = db.relationship('Role', backref='user', lazy='dynamic')
    permission = db.relationship('Permission', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'ID-- <{self.id}>--Username --<{self.username}>-- Password --<{self.password}> --'

class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    member = db.Column(db.Boolean, default=False) 
    manager = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, default=False)
    
    # Relationship
    access = db.relationship('Permission', backref='role', lazy='dynamic')

    def access_level(self):

        if self.member:
            return f'Member: {self.member}'
        elif self.manager:
            return f'Manager: {self.manager}'
        elif self.admin:
            return f'Admin: {self.admin}'
        else:
            'No access level'

    def __repr__(self):
        return self.access_level()


class Permission(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    bronze = db.Column(db.Boolean, default=False) 
    silver = db.Column(db.Boolean, default=False)
    gold = db.Column(db.Boolean, default=False)

    def get_service_level(self):

        if self.bronze:
            return f'Bronze {self.bronze}'
        elif self.silver:
            return f'Silver {self.silver}'
        elif self.gold:
            return f'Gold: {self.gold}'
        else:
            'No Service Level'
    
    def __repr__(self):
        return str(self.get_service_level())

    

class Post(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.Text)

    def __str__(self):
        return f'User: {self.user_id}: {self.text}'


class Car(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    size = db.Column(db.Float)
    boost = db.Column(db.Boolean)

    def __repr__(self):
        return f'User: {self.user} Car name: {self.name}, Size: {self.size}, boost: {self.boost}'


class CustomizedBuildIn(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60))


######################################
#-------<Customized ModelView>-------#
######################################

class CarBlogView(ModelView):
    
    can_delete = True
    page_size = 3
    column_exclude_list = ['id', ]

# Custom Built in templates
class customize_template_built_in(ModelView):

    edit_template = 'custom_edit.html'
    create_template = 'custom_create.html'
    list_template = 'custom_list.html'

# Standalone View
class StandaloneView(BaseView):
    @expose('/')
    def index(self):
        x = get_current_view()
        y = get_url('/')
        print(y)
        print(x.get_url('standalone.index'))
        check_list = ['Fede', 'Bryan', 'John', 'Sara', 'Deborah']
        return self.render('standalone_.html', check_list=check_list)


# Add Admin View
#admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(CarBlogView(Car, db.session))
admin.add_view(customize_template_built_in(CustomizedBuildIn, db.session))

# Grouping Views
admin.add_view(ModelView(User, db.session, category='Membership'))
admin.add_view(ModelView(Role, db.session, category='Membership'))
admin.add_view(ModelView(Permission, db.session, category='Membership'))


# Add arbitrary Hiperlinkscheck_if_db_exists(db)
admin.add_link(MenuLink(name='Home Page', url='/', category='Links'))

# Standalone Views
admin.add_view(StandaloneView(name='Standalone', endpoint='standalone'))




@app.route('/')
def index():
    return redirect(url_for('admin.index'))


@app.route('/test')
def text():

    x = get_current_view()
    y= None
    z = None
    a = None
    b = None
    c = None
    return render_template('index.html', x=x, y=y, z=z, a=a, b=b, c=c)


if __name__ == '__main__':
    check_if_db_exists(db)
    app.run(debug=True)