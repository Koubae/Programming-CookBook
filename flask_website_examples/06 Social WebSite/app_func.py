from app import app, db
from models import User, Tweet, followers
from datetime import datetime


@app.template_filter('time_since')
def time_since(delta):

    '''
    Function that calculates the time past since an action taken, 
    the formula can be used and implement anywhere.
    It needs a datetime object in *delta
    '''
    seconds = delta.total_seconds()
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days > 0:
        return '%dd' % (days)
    elif hours > 0:
        return '%dh' % (hours)
    elif minutes > 0:
        return '%dm' % (minutes)
    else:
        return 'Just now'


def who_to_watch_list(user):
    return User.query.filter(User.id != user.id).order_by(db.func.random()).limit(4).all()

def get_current_time():
    return datetime.now()




