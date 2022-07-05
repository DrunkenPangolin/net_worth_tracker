from flask import render_template, url_for, flash, redirect
from webapp import app, db, bcrypt
from webapp.forms import registration_form, login_form
from webapp.models import User
from flask_login import login_user, logout_user

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("pages/dashboard.html", title="Dashboard")

@app.route("/register", methods=['GET','POST'])
def register():
    form = registration_form()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name = form.first_name.data, last_name = form.last_name.data, email = form.email.data, password = hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.first_name.data} {form.last_name.data}, you are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("pages/register.html", title = 'Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful, please check email and password','danger')
    return render_template("pages/login.html", title = 'Login', form=form)