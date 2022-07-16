import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from webapp import app, db, bcrypt
from webapp.forms import (
    RegistrationForm,
    LoginForm,
    UpdateAccountForm,
    UpdateProfileForm,
    AccountForm,
    SetPasswordForm
)
from webapp.models import Account, User
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/layout")
def layout():
    return render_template("layout.html")


@app.route("/")
def splash():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return render_template("pages/splash.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("pages/dashboard.html", title="Dashboard")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
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
        return redirect(url_for("login"))
    return render_template("user/register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("dashboard"))
        else:
            flash("Login unsuccessful, please check email and password", "danger")
    return render_template("user/login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("dashboard"))


def save_picture(form_picture, user_id):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = user_id + "-" + random_hex + f_ext
    print(picture_fn)
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/profile", methods=["GET", "POST"])
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
        return redirect(url_for("profile"))
    elif request.method == "GET":
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.dob.data = current_user.dob

    return render_template("user/profile.html", title="Profile", form=form)


@app.route("/accounts", methods=["GET", "POST"])
@login_required
def accounts():
    form = AccountForm()
    if form.validate_on_submit():
        account = Account(
            account_name=form.account_name.data,
            account_type=form.account_type.data,
            currency=form.currency.data.split()[0],
            date_opened=form.date_opened.data,
            credit_limit=form.credit_limit.data,
            benefit=form.benefit.data,
            benefit_expiry=form.benefit_expiry.data,
            pin=form.pin.data,
            notes=form.notes.data,
            account_owner=current_user,
        )
        db.session.add(account)
        db.session.commit()
        flash(
            f"Account added",
            "success",
        )
    account_list = Account.query.filter_by(account_owner=current_user).order_by(Account.date_opened.asc())
    return render_template(
        "pages/accounts.html", title="Accounts", form=form, account_list=account_list
    )


@app.route("/account_info/<int:account_id>", methods=["GET", "POST"])
@login_required
def account_info(account_id):
    form = UpdateAccountForm()
    account = Account.query.get_or_404(account_id)
    if account.account_owner != current_user:
        abort(404)
    elif request.method == "GET":
        form.account_name.data = account.account_name
        form.account_type.data = account.account_type
        form.date_opened.data = account.date_opened
        form.date_closed.data = account.date_closed
        form.credit_limit.data = account.credit_limit
        form.benefit.data = account.benefit
        form.benefit_expiry.data = account.benefit_expiry
        form.notes.data = account.notes
    elif form.validate_on_submit():
        account.account_name = form.account_name.data
        account.account_type = form.account_type.data
        account.currency = form.currency.data.split()[0]
        account.date_opened = form.date_opened.data
        account.date_closed = form.date_closed.data
        account.credit_limit = form.credit_limit.data
        account.benefit = form.benefit.data
        account.benefit_expiry = form.benefit_expiry.data
        account.pin = form.pin.data
        account.notes = form.notes.data
        db.session.commit()
        flash(
            f"Account updated",
            "success",
        )

    return render_template(
        "pages/account_info.html",
        account=account,
        form=form,
        title=account.account_name,
    )


@app.route("/account_info/<int:account_id>/delete", methods=["GET", "POST"])
@login_required
def delete_account(account_id):
    account = Account.query.get_or_404(account_id)
    if account.account_owner != current_user:
        abort(404)
    else:
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for("accounts"))


@app.route("/portfolio")
@login_required
def portfolio():
    return render_template("pages/portfolio.html", title="Portfolio")


@app.route("/expenses")
@login_required
def expenses():
    return render_template("pages/expenses.html", title="Expenses")


@app.route("/settings")
@login_required
def settings():
    return render_template("user/settings.html", title="Settings")


@app.route("/site_info")
def site_info():
    return render_template("pages/site_info.html", title="Site Info")


@app.route("/financial_independence")
@login_required
def fi():
    return render_template(
        "pages/financial_independence.html", title="Financial Independence"
    )


@app.route("/documents")
@login_required
def documents():
    return render_template("pages/documents.html", title="Documents")



#not yet completed

@app.route("/set_password", methods=["GET", "POST"])
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
        return redirect(url_for("login"))
    return render_template("user/set_password.html", form=form, title="Set Password")