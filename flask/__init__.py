from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import registration_form, login_form

app = Flask(__name__)

app.config['SECRET_KEY'] = "secrets.token_hex(16)"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)