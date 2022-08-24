from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#creating form class inheriting from FlaskForm
class NameForm(FlaskForm):
    name=StringField("Enter your name", validators=[DataRequired()]) #stringfield class for text field of html                
    submit=SubmitField("Submit") #submitfield class for submit type of html

    