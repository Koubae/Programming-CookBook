import os
# Flask
from flask import Flask, url_for, redirect, render_template, request
from wtforms import form, fields, validators
from werkzeug.security import generate_password_hash, check_password_hash

# Flask_login
import flask_login as login

# Flask_admin
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin import helpers, expose

# Database
from flask_sqlalchemy import SQLAlchemy


# Create Flask Application
app = Flask(__name__)

# Create dummy Secret Key
my_secret = os.urandom(16)


# Config & Create in memory database
app.config['SECRET_KEY'] = my_secret 
app.config['DATABASE_FILE'] = 'database.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
#app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

db = SQLAlchemy(app)

################
#---<MODELS>---#
################

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(64))

    # Flask Login integration
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    #Required for administrative interface
    def __unicode__(self):
        return self.login


######################
#---<FORM & LOGIN>---#
######################

# Login
class LoginForm(form.Form):

    login = fields.StringField(validators=[validators.DataRequired()])
    password = fields.PasswordField(validators=[validators.DataRequired()])

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()

    def validate_login(self, field):
        
        user = self.get_user()
        # Check if User exists
        if user is None:
            print('Withing LoginForm')
            raise validators.ValidationError('Invalid user')
        # Check is password is correct
        if not check_password_hash(user.password, self.password.data):
            raise validators.ValidationError('Invalid Password')


# Registration
class RegistrationForm(form.Form):

    login = fields.StringField(validators=[validators.DataRequired()])
    email = fields.StringField(validators=[validators.DataRequired()])
    password = fields.PasswordField(validators=[validators.DataRequired()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate Username')


##########################
#---<Init Flask_login>---#
##########################

def init_login():

    login_manager = login.LoginManager()
    login_manager.init_app(app)

    #Create User loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


##############################
#---<CUSTOMIZED ModelView>---#
##############################

class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated
        

###############################
#---<CUSTOMIZED Index View>---#
###############################

class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        
        return super(MyAdminIndexView, self).index()

    # Login
    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        
        form = LoginForm(request.form)
        #------------------------------------
        x = form.validate_login
        print(x)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)
    
        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') +'">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        
        return super(MyAdminIndexView, self).index()
        #------------------------------------
    # Sign Up
    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
      
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
       
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


#####################
#---<FLASK VIEWS>---#
#####################

@app.route('/')
def index():
    return render_template('index.html')



#Initialize flask-login
init_login()

# Create Admin
admin = admin.Admin(app, 'Admin Consolview=MyAdminIndexView(), base_template='my_master.html', template_mode='bootstrap3')
e', index_
# Add View
admin.add_view(MyModelView(User, db.session))


def build_sample_db():

    '''
    Populate a small db with some example entries.
    '''

    import string 
    import random
    
    db.drop_all()
    db.create_all()
    #Passwords is hashed, to use plaintext passowrd use instead:
    # text_user = User(login='test', password='test')
    test_user = User(login='fede', password=generate_password_hash('fede'))
    db.session.add(test_user)

    first_names = [
        'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie','Sophie', 'Mia',
        'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
        'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    ]
    last_names = [
        'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
        'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
        'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    ]

    for i in range(len(first_names)):
        user = User()
        user.first_name = first_names[i]
        user.last_name = last_names[i] 
        user.login = user.first_name.lower() 
        user.email = user.login + '@example.com'
        user.password = generate_password_hash(''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10)))
        db.session.add(user)
    db.session.commit()
    return

if __name__ == '__main__':

    # Build a sample db on the fly, if one doesn't exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()
    
    #Start app
    app.run(debug=True)

