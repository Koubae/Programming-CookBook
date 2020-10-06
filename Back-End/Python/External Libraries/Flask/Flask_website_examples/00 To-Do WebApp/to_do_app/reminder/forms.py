from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired


class ReminderForm(FlaskForm):

    title = StringField('title', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])
    tag = SelectField(u'Tag', coerce=int, validators=[InputRequired()])
    submit = SubmitField('Write')

