from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_required, current_user


main = Blueprint("main", __name__)


@main.route("/layout")
def layout():
    return render_template("base/layout.html")


@main.route("/")
def splash():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    return render_template("main/splash.html")


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("main/dashboard.html", title="Dashboard")


@main.route("/portfolio")
@login_required
def portfolio():
    return render_template("main/portfolio.html", title="Portfolio")


@main.route("/expenses")
@login_required
def expenses():
    return render_template("main/expenses.html", title="Expenses")


@main.route("/site_info")
def site_info():
    return render_template("main/site_info.html", title="Site Info")


@main.route("/financial_independence")
@login_required
def fi():
    return render_template("main/financial_independence.html", title="Financial Independence")


@main.route("/documents")
@login_required
def documents():
    return render_template("main/documents.html", title="Documents")
