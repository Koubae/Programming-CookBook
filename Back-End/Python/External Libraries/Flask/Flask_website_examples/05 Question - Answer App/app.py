from flask import Flask, render_template, g, request, session, redirect, url_for, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequestKeyError
import os

# Import DB & Connector
from database import get_db, check_db
from app_query import *
from app_func import *
from mail_client import *


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


# Init DB -from database.py
init_db = check_db(app)

# Close DB at the end of each appcontext
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# @Current User - check
def get_current_user():
    user_result = None
    if 'user' in session:
        user = session['user']
        db = get_db()
        user_cur =  db.execute('select id, name, password, expert, admin from users where name = ?', [user])
        user_result = user_cur.fetchone()
    return user_result

# Index
@app.route('/')
def index():
    user = get_current_user()
    db = get_db()
    # Q_001
    question_cur = db.execute(get_all_qst)
    questions_result = question_cur.fetchall() 
    return render_template('index.html', user=user, questions=questions_result, disabled_token=disabled_token)

# SignUp
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    user = get_current_user()
    if request.method == 'POST':
        db = get_db()
        # Q_002
        existing_user_cur = db.execute(check_if_user_exist, [request.form['name']])
        existing_user = existing_user_cur.fetchone()

        # Check if the user exists
        if existing_user:
            return render_template('signup.html', user=user, error='User already exists!')
        hashed_password = generate_password_hash(request.form['password'], method='sha256')
        # Q_003
        db.execute(inject_new_user, [request.form['name'], hashed_password, '0', '0'])
        db.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', user=user)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    user = get_current_user()
    error = None
    
    if request.method == 'POST':
        db = get_db()

        name = request.form['name']
        password = request.form['password']
        # Q_004
        user_cur = db.execute(login_query, [name])
        user_result = user_cur.fetchone()
        # Check Credentials
        if user_result:
            if check_password_hash(user_result['password'], password):
                session['user'] = user_result['name']
                return redirect(url_for('index'))
            else:
                error = 'The password is incorrect'
        else:
            error = 'The username is incorrect'

    return render_template('login.html', user=user, error=error)

# Logout
@app.route('/logout')
def logout():
    log_out(session)
    return redirect(url_for('index'))

# @User - Ask
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    db = get_db()
    if request.method == 'POST':
        try:
            # Q_006
            db.execute(add_question, [request.form['question'], user['id'], request.form['expert']])
            db.commit()
            return redirect(url_for('index'))
        except BadRequestKeyError as bad_request:
            error = 'Ooops'
            err = BadRequestKeyError
            abort(404)
    # Q_005  / Get a list of experts
    expert_cur = db.execute(experts)
    expert_results = expert_cur.fetchall()

    return render_template('user/ask.html', user=user, experts=expert_results)

# @User/Expert/Admin - Question view
@app.route('/question/<int:question_id>')
def question(question_id):
    user = get_current_user()
    
    db = get_db()
    # Q_007
    question_cur = db.execute(get_question,[question_id])
    question = question_cur.fetchone()
    return render_template('user/question.html', user=user, question=question)

# @Expert Answer   TO DO --> Send email to user, plus direct to anwer qst.
@app.route('/answer/<user_name>/<int:question_id>', methods=['GET', 'POST'])
def answer(user_name, question_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['expert'] == 0:
        return redirect(url_for('index'))
    
    db = get_db()
    
    if request.method == 'POST':
        # TO DO  Send email to User that QST is diab
        if request.form.get('disab', None) == 'Disab':
            # Q_009
            db.execute(inject_answer, [disabled_token, question_id])
            db.commit()
            qst_disabled(user_name, question_id)
            flash('Question disabled')
            return redirect(url_for('index'))
        elif request.form['answer'] == '':
            flash('Please fill up the Answer before submit')
            return redirect(url_for('answer', question_id=question_id))
        # Q_009
        db.execute(inject_answer, [request.form['answer'], question_id])
        db.commit()
        qst_answered(user_name, question_id)
        return redirect(url_for('unanswered'))
    # Q_008
    question_cur = db.execute(question_view, [question_id])
    question = question_cur.fetchone()

    return render_template('expert/answer.html', user=user, question=question, user_name=user_name)

# @Expert - UnAnswered
@app.route('/unanswered')
def unanswered():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['expert'] == 0:
        return redirect(url_for('index'))
    db = get_db()
    if user['admin'] == 1:
        # Q_11
        question_cur = db.execute(unanswered_admin)
    else:
        # Q_10
        question_cur = db.execute(unanswered_qst, [user['id']])
    questions = question_cur.fetchall()

    return render_template('expert/unanswered.html', user=user, questions=questions)


# @Admin - User List
@app.route('/users')
def users():
    '''
    To Create the first user admin, open database (sqlite3 [database.db]) and run this code
    update users set admin = '1' where id = 1;
    '''
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['admin'] == 0:
        return redirect(url_for('index'))
    
    db = get_db()
    # Q_12
    users_cur = db.execute(query_users)
    users_results = users_cur.fetchall()
    return render_template('admin/users.html', user=user, users=users_results)


# Need to add more functionality to the Admin 
# @Admin - Promote
@app.route('/promote/<int:user_id>')
def promote(user_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['admin'] == 0:
        return redirect(url_for('index'))
   
    db = get_db()
    # Q_13
    get_access_level = db.execute(check_access_level, [user_id])
    get_access = get_access_level.fetchone()
    if get_access[2] == 1:
        flash("Admin can't be promoted as Expert...Admin has all expert's privilages already!")
        return redirect(url_for('users'))
    elif get_access[1] == 1:
        # Q_14
        promote_exp = db.execute(remove_promotion, [user_id])
        db.commit()
        flash("Expert Downgraded to User")
        return redirect(url_for('users'))
    else:
        # Q_15
        promote_exp = db.execute(add_promotion, [user_id])
        db.commit()
        return redirect(url_for('users'))

@app.route('/useradd', methods=['GET', 'POST'])
def new_user():

    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['admin'] == 0:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        db = get_db()
        # Q_002
        existing_user_cur = db.execute(check_if_user_exist, [request.form['name']])
        existing_user = existing_user_cur.fetchone()
        if existing_user:
            flash('User already exists!')
            return redirect(url_for('new_user'))
        user_role = request.form['role']
        hashed_password = generate_password_hash(request.form['password'], method='sha256')
        if user_role == 'Member':
            db.execute(inject_new_user, [request.form['name'], hashed_password, '0', '0'])
            db.commit()
            flash('New Member Created')
        elif user_role == 'Expert':
            db.execute(inject_new_user, [request.form['name'], hashed_password, '1', '0'])
            db.commit()
            flash('New Expert Created')
        elif user_role == 'Admin':
            db.execute(inject_new_user, [request.form['name'], hashed_password, '0', '1'])
            db.commit()
            flash('New Admin Created')
        return redirect(url_for('new_user'))     

    return render_template('admin/new_user.html', user=user)
   

# Error Handler, 404
@app.errorhandler(404)
def error_404(error):
    '''
    Error for page not found
    '''
    return render_template('error_pages/404.html', error=error), 404
if __name__ == '__main__':
    app.run(debug=True)