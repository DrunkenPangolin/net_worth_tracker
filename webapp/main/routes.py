from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from webapp import app, db, bcrypt, mail
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
from flask_mail import Message


main = Blueprint("main", __name__)



@main.route("/layout")
def layout():
    return render_template("layout.html")


@main.route("/")
def splash():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return render_template("pages/splash.html")


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("pages/dashboard.html", title="Dashboard")


@main.route("/portfolio")
@login_required
def portfolio():
    return render_template("pages/portfolio.html", title="Portfolio")


@main.route("/expenses")
@login_required
def expenses():
    return render_template("pages/expenses.html", title="Expenses")


@main.route("/site_info")
def site_info():
    return render_template("pages/site_info.html", title="Site Info")


@main.route("/financial_independence")
@login_required
def fi():
    return render_template("pages/financial_independence.html", title="Financial Independence")


@main.route("/documents")
@login_required
def documents():
    return render_template("pages/documents.html", title="Documents")
