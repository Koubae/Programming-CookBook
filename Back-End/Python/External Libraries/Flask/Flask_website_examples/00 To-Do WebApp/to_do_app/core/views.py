from flask import render_template, Blueprint, flash, request, redirect, url_for
from to_do_app.models import Tag, Reminder

# Internal import
from to_do_app import db


core = Blueprint('core', __name__)

@core.route('/home')
@core.route('/')
def index():

    page = request.args.get('page', 1, type=int)
    all_reminder = Reminder.query.order_by(Reminder.reminder_date.desc()).paginate(page=page, per_page=10)
    all_tags = Tag.query.filter_by(tag=Tag.tag)
    
    return render_template('index.html', all_reminder=all_reminder, tag=all_tags)

# Special View by filter_by Tag 
@core.route('/view/<tag>')
def tag_view(tag):

    page = request.args.get('page', 1, type=int)
    tag_id = Tag.query.filter_by(tag=tag).first()
    tag_ = tag_id.id
    view_tag = Reminder.query.get(tag_)
    order_tag = Reminder.query.filter_by(tag=tag_id).order_by(Reminder.reminder_date.desc()).paginate(page=page, per_page=10)
    all_tags = Tag.query.filter_by(tag=Tag.tag)  

    return render_template('tag/tag_view.html', view_tag=view_tag, order_tag=order_tag, tag=all_tags)

# Special View by filter_by user's search  
@core.route('/search', methods=['GET', 'POST'])
@core.route('/read/search', methods=['GET', 'POST'])
@core.route('/view/search', methods=['GET', 'POST'])
def search():

    page = request.args.get('page', 1, type=int)

    if request.method == 'POST':
        word_search = request.form['search']        
        search_query = Reminder.query.order_by(Reminder.tag_id).paginate(page=page, per_page=10)      
    
    return render_template('search.html', search_query= search_query, word_search=word_search)