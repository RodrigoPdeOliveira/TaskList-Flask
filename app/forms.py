from flask_wtf import FlaskForm
from wtforms.validators import EqualTo, InputRequired, Optional
from wtforms import (
    StringField, DateTimeLocalField, TextAreaField
)


class RegisterForm(FlaskForm):
    name = StringField('Username: ', [InputRequired()])
    password = StringField('Password: ', [
            InputRequired(),
            EqualTo('confirm', message='Passwords must match.')
        ])
    confirm = StringField('Confirm password: ', [InputRequired()])


class LoginForm(FlaskForm):
    name = StringField('Username: ', [InputRequired()])
    password = StringField('Password: ', [InputRequired()])


class TaskForm(FlaskForm):
    title = StringField('Title: ', [InputRequired()])
    about = TextAreaField('Description: ', [Optional()])
    date = DateTimeLocalField('Ends on: ', [Optional()])
