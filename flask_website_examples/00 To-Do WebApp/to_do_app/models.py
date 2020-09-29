from to_do_app import db
from datetime import datetime


# Post
class Reminder(db.Model):
    
    __tablename__ = 'reminders'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    text = db.Column(db.Text, nullable=False)
    reminder_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relationships
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)
    tag = db.relationship('Tag', backref=db.backref('reminders', lazy=True))

    def __init__(self, title, text, tag_id):
        self.title = title
        self.text = text
        self.tag_id = tag_id
        

    def __repr__(self):
        return f' ID: {self.id} --- Title: {self.title} --- Text.. --- Date:{self.reminder_date} --- TAG_ID: {self.tag_id} TAG:{self.tag} ---'
    

# Tag
class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(32), nullable=False, unique=True)

    def __init__(self, tag):
        self.tag = tag

    def __repr__(self):
        return f'{self.tag}'