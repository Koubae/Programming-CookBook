from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# internal imports
from to_do_app.models import Tag


class TagForm(FlaskForm):
    
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Create')
    
    # Check if the tag aleady exists
    def check_tag(self, tag):
        if Tag.query.filter_by(tag=tag.data).first():
            return 'Tag Already Exists'
