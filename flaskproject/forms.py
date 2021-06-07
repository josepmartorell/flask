from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class NoteForm(Form):
    subject = StringField('subject', validators=[DataRequired(message='Please enter note subject')])
    detail = TextAreaField('detail')
