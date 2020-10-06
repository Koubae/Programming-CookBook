from app import app, photos, db
from models import User, Tweet, followers
from forms import RegisterForm, LoginForm, TweetForm, UpdatePic
from flask import render_template, redirect, url_for, request, abort, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import login_required, login_user, current_user, logout_user
from sqlalchemy.exc import IntegrityError

from app_func import who_to_watch_list, get_current_time


# Home
@app.route('/')
def index():
    form = LoginForm()
    form_2 = TweetForm()

    page = request.args.get('page', 1, type=int)

    all_tweets = Tweet.query.order_by(Tweet.date_created.desc()).paginate(page=page, per_page=10)
    current_time = get_current_time()
    
    return render_template('index.html', form=form, form_2=form_2, logged_in_user=current_user, all_tweets=all_tweets,  current_time=current_time)

# Signup
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            if form.image.data:
                image_filename = photos.save(form.image.data)
                image_url = photos.url(image_filename)

                new_user = User(name=form.name.data, username=form.username.data, image=image_url, password=generate_password_hash(form.password.data), join_date=datetime.now())
            else:
                new_user = User(name=form.name.data, username=form.username.data, password=generate_password_hash(form.password.data), join_date=datetime.now())
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError as err:
            print(repr(err))
            flash('User already exists')
            return redirect(url_for('index'))


        login_user(new_user)
        return redirect(url_for('profile'))
    return render_template('register.html', form=form)


# Loging
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
    
        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            
            return render_template('index.html', form=form, message='Login Failed', logged_in_user=current_user)
        
        if check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('profile'))
        return render_template('index.html', form=form, message='Wrong Password', logged_in_user=current_user)
        
    return render_template('index.html', form=form, logged_in_user=current_user)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Profile
@app.route('/profile', defaults={'username' : None})
@app.route('/profile/<username>')
@login_required
def profile(username):
    
    form = UpdatePic()
    form_2 = TweetForm()

    if username:
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('User does not exist')
            abort(404)
    else:
        user = current_user
 
    tweets = Tweet.query.filter_by(user=user).order_by(Tweet.date_created.desc()).all()
   
    display_follow = True
    change_pic = False
    if current_user == user:
        display_follow = False
        change_pic = True
    elif current_user in followed_by: 
        display_follow = False
        change_pic = False
    whot_to_watch = who_to_watch_list(user)
    
    return render_template('profile.html', current_user=user, tweets=tweets, current_time= get_current_time(), followed_by=user.followed_by.all(), display_follow=display_follow, who_to_watch=whot_to_watch, logged_in_user=current_user, form=form, form_2=form_2, change_pic=change_pic)


#Update Pic  
@app.route('/update_pic', methods=['POST'])
@login_required
def update_pic():

    form = UpdatePic()
    user = User.query.filter_by(username=current_user.username).first()
    if form.validate():
        image_filename = photos.save(form.image.data)
        image_url = photos.url(image_filename)
        user.image =  image_url
        db.session.commit()
        return redirect(url_for('profile', username=current_user.username))
    flash('Something went wrong')
    return redirect(url_for('index'))


@app.route('/timeline', defaults={'username' : None})
@app.route('/timeline/<username>')
@login_required
def timeline(username):

    form = TweetForm()
    form_2 = TweetForm()

    if username:
        user = User.query.filter_by(username=username).first()
        if not user:
            abort(404)
        
        tweets = Tweet.query.filter_by(user=user).order_by(Tweet.date_created.desc()).all()
        total_tweets = len(tweets)
    else:
        user = current_user
        tweets = Tweet.query.join(followers, (followers.c.followee_id == Tweet.user_id)).filter(followers.c.follower_id == current_user.id).order_by(Tweet.date_created.desc()).all()
        total_tweets = Tweet.query.filter_by(user=user).order_by(Tweet.date_created.desc()).count()

    current_time = get_current_time()
    followed_by_count = user.followed_by.count()
    who_to_watch = who_to_watch_list(user)

    return render_template('timeline.html', form=form, form_2=form_2, tweets=tweets, current_time=current_time, current_user=user, total_tweets=total_tweets, who_to_watch=who_to_watch, logged_in_user=current_user, followed_by_count=followed_by_count)

# Followers
@app.route('/followers', defaults={'username' : None})
@app.route('/followers/<username>')
@login_required
def followers(username):

    form_2 = TweetForm()
    if username:
        user = User.query.filter_by(username=username).first()
        if not user:
            abort(404)
    else:
        user = current_user
    
    all_followers = user.followed_by    
    return render_template('followers.html', followers=all_followers, form_2=form_2)

# Post Tweet   
@app.route('/post_tweet', methods=['POST'])
@login_required
def post_tweet():

    form = TweetForm()
    if form.validate():
        tweet = Tweet(user_id=current_user.id, text=form.text.data, date_created=datetime.now())
        db.session.add(tweet)
        db.session.commit()
        user = current_user.username
        return redirect(url_for('timeline', username=current_user.username))
    flash('Something went wrong')
    return redirect(url_for('index'))



# Follow   
@app.route('/follow/<username>')
@login_required
def follow(username):
    
    user_to_follow = User.query.filter_by(username=username).first()
    current_user.following.append(user_to_follow)
    db.session.commit()

    return redirect(url_for('profile'))

# Error Handler, 404
@app.errorhandler(404)
def error_404(error):
    '''
    Errorhandler for 404 HTTP status code
    '''
    return render_template('error_pages/404.html', error=error), 404

# Error Handler, 403
@app.errorhandler(403)
def error_404(error):
    '''
    Errorhandler for 403 HTTP status code
    '''
    return render_template('error_pages/403.html', error=error), 403

# Error Handler, 500
@app.errorhandler(500)
def error_404(error):
    '''
    Errorhandler for 500 HTTP status code
    '''
    return render_template('error_pages/500.html', error=error), 500

