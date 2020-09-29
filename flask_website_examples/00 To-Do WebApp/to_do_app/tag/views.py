from flask import render_template, Blueprint, url_for, flash, redirect, request

# internal Imports
from to_do_app import db
from to_do_app.tag.forms import TagForm
from to_do_app.models import Tag


tag_bp = Blueprint('tag_bp', __name__)

# Create a New Tag
@tag_bp.route('/create_tag', methods=['GET', 'POST'])
def create_tag():

    form = TagForm()

    if form.validate_on_submit():
        # Check if tag already exists
        if form.check_tag(form.tag):
            err = form.check_tag(form.tag)
            flash(err)
            return redirect(url_for('tag_bp.create_tag'))
        else:
            new_tag = form.tag.data
            new_tag = new_tag.strip()
            tag = Tag(tag=new_tag)
            
            db.session.add(tag)
            db.session.commit()
            flash(f'Tag ---- {tag.tag} --- Created Succesfully!')
            return redirect(url_for('tag_bp.create_tag'))

    return render_template('tag/create_tag.html', form=form)