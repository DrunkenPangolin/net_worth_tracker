from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registration_form(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(max=20),
            ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(max=20),
            ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email(),
            ])
    password = PasswordField('Password',
        validators=[
            DataRequired(),
            ])
    confirm_password = PasswordField('Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password'),
            ])
    submit = SubmitField('Register')


class login_form(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email(),
            ])
    password = PasswordField('Password',
        validators=[
            DataRequired(),
            ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')