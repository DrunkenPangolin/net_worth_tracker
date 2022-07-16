from webapp import db, login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False)
    dob = db.Column(db.DateTime)
    profile_pic = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    accounts = db.relationship("Account", backref="account_owner", lazy=True)

    def __repr__(self):
        return f"User('{self.name}','{self.email}','{self.profile_pic}')"


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String, nullable=False)
    account_type = db.Column(db.String, nullable=False)
    currency = db.Column(db.String(3))
    date_opened = db.Column(db.Date, nullable=False)
    date_closed = db.Column(db.Date)
    credit_limit = db.Column(db.Integer, default=0)
    benefit = db.Column(db.String)
    benefit_expiry = db.Column(db.Date)
    pin = db.Column(db.String)
    notes = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Account('{self.account_name}','{self.account_type}','{self.currency}','{self.notes}')"
 