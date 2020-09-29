from flask import Flask, session, request, render_template, redirect, url_for, flash
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(20)

# No real meaning to it, just for training purposes
user_type = ['Admin', 'Supervisor', 'Moderator', 'Member']

# To DO- implement as python decorator
# Check if User in session

def user_logged():
    if 'name' in session:
        name = session['name']
        return name
    flash('You must log in!')


   
# Index
@app.route('/', methods=['GET', 'POST'])
def index():

    check_user = user_logged()
    if not check_user:
        return redirect(url_for('signup'))

    return render_template('index.html', logged=check_user)

# Sign Up
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    user_list = user_type

    return render_template('session/signup.html', user_list=user_list, logged=None)

# Log Out
@app.route('/logout', methods=['GET', 'POST'])
def logout():

    check_user = user_logged()
    if check_user:
        session['name'] = None
        flash('You have logged out')
        return redirect(url_for('index'))
    '''
    Another way, less elegant to implement a logout. Leaving it as referance for training purposes. 
    '''
    # if 'name' in session:
    #     session['name'] = None
    #     flash('You have logged out')
    #     return redirect(url_for('index'))


# Welcome Page
@app.route('/welcome',  methods=['GET', 'POST'])
def welcome():
    ''''
    After log in with a user, it will redirect to the welcome page, this is only meant to show that the user 
    lays within the session
    '''
    
    name = ''
    where = ''
    role = ''
    # Prepopulate Welcome Page after User "SignUp" From def signup():
    if request.method == 'POST':
        name = request.form['name']
        where = request.form['where']
        role = request.form['select']
        session['name'] = name
        session['ROLE'] = role
        check_user = user_logged()
        return render_template('request/welcome.html', name=name, location=where, role=role, logged=check_user) 
    else:
        if 'name' in session:
            name = session['name']
            role = session['ROLE']
            flash('Welcome')
            return redirect(url_for('profile', name=name, role=role))
    
    check_user = user_logged()
    if not check_user:
        return redirect(url_for('signup'))
            
    


# Profile Page
@app.route('/profile/<name>', methods=['GET', 'POST'])
def profile(name):
    check_user = user_logged()
    if not check_user:
        return redirect(url_for('signup'))

    usr_name = name
    role = request.args.get('role')

    return render_template('session/profile.html', name=usr_name, role=role, logged=check_user)


# Select Theme Dark / Light
@app.route('/theme', methods=['GET', 'POST'])
def theme():

    check_user = user_logged()
    if not check_user:
        return redirect(url_for('signup'))

    if check_user:
        user_mode = request.form
        if user_mode.get('light'):
            session['MODE'] = user_mode.get('light')
            new_mode = session['MODE']
            flash(f'Mode is {new_mode}')
            return redirect(url_for('index'))
        elif user_mode.get('dark'):
            session['MODE'] = user_mode.get('dark')
            new_mode = session['MODE']
            flash(f'Mode is {new_mode}')
            return redirect(url_for('index'))
       
        return render_template('session/theme.html', logged=check_user)
 



# Check if anyone in the session
@app.route('/session/')
def session_1():

    check_user = user_logged()
    if not check_user:
        return redirect(url_for('signup'))

    if 'name' in session:
        name = session['name']
        if 'MODE' in session:
            mode = session['MODE']
            return render_template('session/session_1.html', name=name, logged=check_user, mode=mode)        
        return render_template('session/session_1.html', name=name, logged=check_user)
    else:
        print('no user')
        return render_template('session/session_1.html', logged=check_user)

# Search bar
#TO Do- For the moment is just taking inputs and do stuff with that, need to implement a database
@app.route('/search/')
def search():
    check_user = user_logged()
    if not check_user:
        return redirect(url_for('signup'))
    result = request.args.get('search')
    result *= 2    
    return render_template('request/args_get.html', result=result, logged=check_user)


# QUery String, play a bit with request.args.get
@app.route('/request', methods=['GET', 'POST'])
def my_request():

    name = request.args.get('name')
    location = request.args.get('where')
    check_user = user_logged() 

    if request.method == 'POST':
        flash('Succesfully Posted')
        return render_template('request/query_string.html', logged=check_user, name=name, location=location)
    return render_template('request/query_string.html', logged=check_user, name=name, location=location)


if __name__ == '__main__':
    app.run(debug=True)