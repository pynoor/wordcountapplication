from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired

class WordForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Count words!')
