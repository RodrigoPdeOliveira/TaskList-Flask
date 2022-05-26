from flask_wtf import FlaskForm
from wtforms.validators import EqualTo, InputRequired, Optional
from wtforms import (
    StringField, DateTimeLocalField, TextAreaField, PasswordField
)


class RegisterForm(FlaskForm):
    name = StringField('Username: ', [InputRequired()])
    password = PasswordField('Password: ', [
            InputRequired(),
            EqualTo('confirm', message='Passwords must match.')
        ])
    confirm = PasswordField('Confirm password: ', [InputRequired()])


class LoginForm(FlaskForm):
    name = StringField('Username: ', [InputRequired()])
    password = PasswordField('Password: ', [InputRequired()])


class TaskForm(FlaskForm):
    title = StringField('Title: ', [InputRequired()])
    about = TextAreaField('Description: ', [Optional()])
    date = DateTimeLocalField(
            label='Ends on: ',
            validators=[InputRequired()],
            format='%Y-%m-%dT%H:%M'
        )


class NewPassword(FlaskForm):
    old_password = PasswordField('Old password: ', [InputRequired()])
    new_password = PasswordField('New password: ', [
        InputRequired(),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm new password: ', [InputRequired()])


class NewUsername(FlaskForm):
    new_username = StringField('New username: ', [InputRequired()])
    password = PasswordField('Confirm your password: ', [InputRequired()])
