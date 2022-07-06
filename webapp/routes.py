from flask import render_template, url_for, flash, redirect, request
from webapp import app, db, bcrypt
from webapp.forms import RegistrationForm, LoginForm
from webapp.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("pages/dashboard.html", title="Dashboard")

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            password = hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.first_name.data} {form.last_name.data}, you are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("pages/register.html", title = 'Register', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful, please check email and password','danger')
    return render_template("pages/login.html", title = 'Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('dashboard'))


@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('pages/account.html', title='Account', image_file = image_file)