from email.policy import default
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_login import current_user
from wtforms import (
    StringField,
    SubmitField,
    DateField,
    IntegerField,
    SelectField,
)
from wtforms.validators import InputRequired, ValidationError
from webapp.models import Account, User
from webapp.form_lists import account_types, currencies
from werkzeug.utils import secure_filename



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
    credit_limit = IntegerField("Credit Limit", default=0)
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


class CloseAccountForm(FlaskForm):
    date_closed = DateField("Date Closed")
    submit = SubmitField("Close Account")


class CSVUploadForm(FlaskForm):
    file = FileField("Upload CSV", validators=[FileAllowed(["csv"])])
    submit = SubmitField("Upload CSV")
