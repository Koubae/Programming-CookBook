from app import db, login_manager
from flask_login import UserMixin


followers = db.Table('follower',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followee_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    image = db.Column(db.String(100), nullable=False, default='static/img/anonymous.png')
    password = db.Column(db.String(50))
    join_date = db.Column(db.DateTime)

    tweets = db.relationship('Tweet', backref='user', lazy='dynamic')

    following = db.relationship('User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followee_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    
    followed_by = db.relationship('User', secondary=followers,
        primaryjoin=(followers.c.followee_id == id),
        secondaryjoin=(followers.c.follower_id == id),
        backref=db.backref('followees', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return f'ID:<{self.id}> -- Name:<{self.name}> -- username:<{self.username}> -- join_date:<{self.join_date}>'


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String(140), nullable=False)
    date_created = db.Column(db.DateTime)

    def __repr__(self):
        return f'ID:<{self.id}> -- user_id:<{self.user_id}>  -- Date:<{self.date_created}>'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


