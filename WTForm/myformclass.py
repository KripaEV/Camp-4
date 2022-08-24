from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#creating form class inheriting from FlaskForm
class NameForm(FlaskForm):
    name=StringField("Enter your name", validators=[DataRequired()])
    submit=SubmitField("Submit")