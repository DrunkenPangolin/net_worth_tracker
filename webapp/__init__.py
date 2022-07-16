from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "f1168d879d255c586c08c99b84b06f82"  # secrets.token_hex(16)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../nw_private/site.db"
db = SQLAlchemy(app)
# db.create_all() #<-- wondering if this is necessary?
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from webapp import routes
