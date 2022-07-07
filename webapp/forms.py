from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webapp.models import Accounts, User


class RegistrationForm(FlaskForm):
    first_name = StringField(
        "First Name",
        validators=[
            DataRequired(),
            Length(max=20),
        ],
    )
    last_name = StringField(
        "Last Name",
        validators=[
            DataRequired(),
            Length(max=20),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=100),
        ],
    )
    dob = DateField(
        "Date of birth"
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password"),
        ],
    )
    submit = SubmitField("Register")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is already registered")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateProfileForm(FlaskForm):
    first_name = StringField(
        "First Name",
        validators=[
            DataRequired(),
            Length(max=20),
        ],
    )
    last_name = StringField(
        "Last Name",
        validators=[
            DataRequired(),
            Length(max=20),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=100),
        ],
    )
    dob = DateField(
        "Date of birth"
    )
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is already registered")



class AddAccountForm(FlaskForm):
    account_name = StringField(
        "Account Name",
        validators=[
            DataRequired(),
        ],
    )
    account_type = StringField(
        "Account Type",
        validators=[
            DataRequired(),
        ],
    )
    currency = StringField(
        "Currency",
        validators=[DataRequired(),
        Length(min=3, max=3)
        ]
    )
    date_opened = DateField(
        "Date Opened",
        validators=[
            DataRequired(),
        ],
    )
    credit_limit = FloatField("Credit Limit")
    benefit = StringField(
        "Account Benefit",
    )
    benefit_expiry = DateField("Benefit Expiry")
    pin = StringField("PIN")
    notes = StringField(
        "Notes",
    )
    submit = SubmitField("Add")


    def validate_type(self, type):
        accepted_account_types = ['Travel Card', 'Savings Account', 'Credit Card' ,'Current Account']
        if type.data not in accepted_account_types:
            raise ValidationError(f"Type must be one of the following: {account_types}")

    def validate_account_name(self, account_name):
        account = Accounts.query.filter_by(account_name=account_name.data).first()
        if account:
            raise ValidationError("That account name is already registered")