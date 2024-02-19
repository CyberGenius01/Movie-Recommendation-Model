from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class DataEntry(FlaskForm):
    
    value = StringField(label='Search for Movies', validators=[DataRequired()])
    category = RadioField(label='Choose the search category:', choices=['Name', 'Genre', 'Keyword', 'Cast'], validators=[DataRequired()], default='Name')
    submit = SubmitField(label='Recommend movies')