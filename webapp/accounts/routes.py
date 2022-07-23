from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from webapp import db
from webapp.accounts.forms import (
    UpdateAccountForm,
    AccountForm,
)
from webapp.models import Account, User
from flask_login import current_user, login_required
from flask_mail import Message


accounts = Blueprint("accounts", __name__)


@accounts.route("/accounts", methods=["GET", "POST"])
@login_required
def accounts_page():
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
        "main/accounts.html", title="Accounts", form=form, account_list=account_list
    )
    
    
@accounts.route("/account_info/<int:account_id>", methods=["GET", "POST"])
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
        "main/account_info.html",
        account=account,
        form=form,
        title=account.account_name,
    )


@accounts.route("/account_info/<int:account_id>/delete", methods=["GET", "POST"])
@login_required
def delete_account(account_id):
    account = Account.query.get_or_404(account_id)
    if account.account_owner != current_user:
        abort(404)
    else:
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for("accounts.accounts_page"))
