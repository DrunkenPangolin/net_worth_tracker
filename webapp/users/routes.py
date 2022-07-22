import os
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from webapp import app, db, bcrypt
from webapp.models import User, Account
from webapp.users.forms import (
    RegistrationForm,
    LoginForm,
    UpdateProfileForm,
    SetPasswordForm,
)
from webapp.users.utils import save_picture, send_reset_email


users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(
            name=form.name.data,
            email=form.email.data,
            dob=form.dob.data,
            password=hashed_pass,
        )
        db.session.add(user)
        db.session.commit()
        flash(
            f"Profile created for {form.name.data}, you are now able to log in",
            "success",
        )
        return redirect(url_for("users.login"))
    return render_template("user/register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.dashboard"))
        else:
            flash("Login unsuccessful, please check email and password", "danger")
    return render_template("user/login.html", title="Login", form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.dashboard"))


@users.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            old_pic = current_user.profile_pic
            picture_file = save_picture(form.picture.data, str(current_user.id))
            current_user.profile_pic = picture_file
            if old_pic != "default.jpg":
                os.remove(os.path.join(app.root_path, "static/profile_pics", old_pic))

        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.dob = form.dob.data
        db.session.commit()
        flash("Your profile has been updated!", "success")
        return redirect(url_for("users.profile"))
    elif request.method == "GET":
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.dob.data = current_user.dob

    return render_template("user/profile.html", title="Profile", form=form)


#not yet completed
@users.route("/set_password", methods=["GET", "POST"])
def set_password():
    form = SetPasswordForm()
    if form.validate_on_submit():
        if current_user:
            current_user.password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        else:
            #presumably there is no 'current_user' if the user follows a forgotten password link
            return
        db.session.commit()
        flash(
            f"Password changed successfully",
            "success",
        )
        return redirect(url_for("users.login"))
    return render_template("user/set_password.html", form=form, title="Set Password")