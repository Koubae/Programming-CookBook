from flask import redirect, render_template, Blueprint, url_for, request, flash

# Internal Reminder
from to_do_app import db
from to_do_app.models import Reminder, Tag
from to_do_app.reminder.forms import ReminderForm


reminder = Blueprint('reminder', __name__)
# Create
@reminder.route('/write', methods=['GET', 'POST'])
def write_reminder():
    
    form = ReminderForm()
    tags = db.session.query(Tag).filter_by(id=Tag.id).all()
    tag_list = [(tag.id, tag.tag) for tag in tags]
    form.tag.choices = tag_list 
    
    if request.method == 'POST':    
        if form.validate_on_submit():
            new_rem = Reminder(title=form.title.data,
                            text=form.body.data,
                            tag_id=form.tag.data
                            )        
            db.session.add(new_rem)
            db.session.commit()
            flash(f'New Reminder created, title {new_rem.title}')
            return redirect(url_for('core.index'))     
               
    return render_template('reminder/write_reminder.html', form=form)

# Read
@reminder.route('/read/<int:reminder_id>')
def read_reminder(reminder_id):
    
    reminder = Reminder.query.get_or_404(reminder_id)
    return render_template('reminder/read_reminder.html', post=reminder, title=reminder.title, date=reminder.reminder_date, tag=reminder.tag)

# Update
@reminder.route('/<int:reminder_id>/update', methods=['GET', 'POST'])
def update_reminder(reminder_id):

    reminder = Reminder.query.get_or_404(reminder_id)
    tags = db.session.query(Tag).filter_by(id=Tag.id).all()
    tag_list = [(tag.id, tag.tag) for tag in tags]
    form = ReminderForm()
    form.tag.choices = tag_list
    print(reminder.tag_id)

    if form.validate_on_submit():
        reminder.title = form.title.data
        reminder.text = form.body.data
        reminder.tag_id = form.tag.data
        
        db.session.commit()
        flash(f'{reminder.title} Reminder Updated')
        return redirect(url_for('core.index', reminder_id=reminder_id))

    if request.method == 'GET':
        form.title.data = reminder.title
        form.body.data = reminder.text


    return render_template('reminder/write_reminder.html', title='Update', form=form)

# Delete
@reminder.route('/<int:reminder_id>/delete', methods=['GET', 'POST'])
def delete_reminder(reminder_id):
    
    
    reminder = Reminder.query.get_or_404(reminder_id)
    if request.method == 'POST':
        form = request.form['delete']
        if form == 'Delete': 
            db.session.delete(reminder)
            db.session.commit()
            return redirect(url_for('core.index'))
            flash('Reminder  Deleted')

    return redirect(url_for('core.index'))