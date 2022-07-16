from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    DateField,
    IntegerField,
    SelectField,
)
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from webapp.models import Account, User
from webapp.form_lists import account_types, currencies


class RegistrationForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            InputRequired(),
            Length(max=30),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            InputRequired(),
            Email(),
            Length(max=100),
        ],
    )
    dob = DateField("Date of birth")
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
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
            InputRequired(),
            Email(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateProfileForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            InputRequired(),
            Length(max=30),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            InputRequired(),
            Email(),
            Length(max=100),
        ],
    )
    dob = DateField("Date of birth")
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is already registered")


class AccountForm(FlaskForm):
    account_name = StringField(
        "Account Name",
        validators=[
            InputRequired(),
        ],
    )
    account_type = SelectField(
        "Account Type",
        choices=account_types,
        validators=[
            InputRequired(),
        ],
    )
    currency = SelectField(
        "Currency Code",
        choices=currencies,
        validators=[
            InputRequired(),
        ],
    )
    date_opened = DateField(
        "Date Opened",
        validators=[
            InputRequired(),
        ],
    )
    credit_limit = IntegerField("Credit Limit")
    benefit = StringField(
        "Account Benefit",
    )
    benefit_expiry = DateField("Benefit Expiry")
    pin = StringField("PIN")
    notes = StringField(
        "Notes",
    )
    submit = SubmitField("Add Account")

    def validate_account_name(self, account_name):
        account = Account.query.filter_by(
            account_name=account_name.data, user_id=current_user.id
        ).first()
        if account:
            raise ValidationError("That account name is already registered")


class UpdateAccountForm(FlaskForm):
    account_name = StringField(
        "Account Name",
        validators=[
            InputRequired(),
        ],
    )
    account_type = SelectField(
        "Account Type",
        choices=account_types,
        validators=[
            InputRequired(),
        ],
    )
    currency = SelectField(
        "Currency Code",
        choices=currencies,
        validators=[
            InputRequired(),
        ],
    )
    date_opened = DateField(
        "Date Opened",
        validators=[
            InputRequired(),
        ],
    )
    date_closed = DateField("Date Closed")
    credit_limit = IntegerField("Credit Limit")
    benefit = StringField(
        "Account Benefit",
    )
    benefit_expiry = DateField("Benefit Expiry")
    pin = StringField("PIN")
    notes = StringField(
        "Notes",
    )
    submit = SubmitField("Update")

    def validate_account_name(self, account_name):
        account = Account.query.filter_by(
            account_name=account_name.data, user_id=current_user.id 
        ).first()
        if account:
            print ('account id =',account.id)
            raise ValidationError("That account name is already registered")


class ForgottenPasswordForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            InputRequired(),
            Email(),
            Length(max=100),
        ],
    )
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("There is no account linked to that email")



class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            ],
        )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo("password"),
            ],
        )
    submit = SubmitField("Submit")

    
