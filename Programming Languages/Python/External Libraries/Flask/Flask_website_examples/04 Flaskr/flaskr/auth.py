import functools 

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flaskr.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


#  Login Wrapper
def login_required(view):

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view


@bp.before_app_request
def load_logged_in_user():

    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id, )).fetchone()
        )

#  Sign up
@bp.route('/register', methods=('GET', 'POST'))
def register():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif (
            db.execute('SELECT id FROM user WHERE username = ?', (username, )).fetchone()
            is not None
        ):
            # User Exists
            error = f'User {username} is already taken.'
        
        if error is None:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?,?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
            return redirect(url_for('auth.login'))
        
        flash(error)
    
    return render_template('auth/register.html')


# Login 
@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute (
            'SELECT * FROM user WHERE username = ?', (username, )
        ).fetchone()

        if user is None:
            error = 'Incorrect Username'
        elif not check_password_hash(user['password'], password):
            error = 'incorrect password'
        
        if error is None:
            #Store User is in new Seesion
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)
    return render_template('auth/login.html')


# Logout
@bp.route('/logout')
def logout():

    session.clear()
    return redirect(url_for('index'))