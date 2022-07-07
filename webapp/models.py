from webapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.DateTime)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.first_name}','{self.last_name}','{self.email}','{self.image_file}')"


class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    country = db.Column(db.String)
    date_opened = db.Column(db.Date, nullable=False)
    date_closed = db.Column(db.Date)
    credit_limit = db.Column(db.Float)
    benefit = db.Column(db.String)
    benefit_expiry = db.Column(db.Date)
    pin = db.Column(db.String)
    notes = db.Column(db.String)

    def __repr__(self):
        return 