import os
from flask import abort, Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from flask_mail import Message
from webapp import app, db
from webapp.accounts.forms import AccountForm, CloseAccountForm, CSVUploadForm, UpdateAccountForm
from webapp.models import Account, User
from werkzeug.utils import secure_filename


accounts = Blueprint("accounts", __name__)


@accounts.route("/accounts", methods=["GET", "POST"])
@login_required
def accounts_page(closed=False):
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

    if closed == False:
        account_list = Account.query.filter_by(account_owner=current_user).filter_by(date_closed=None).order_by(Account.date_opened.asc())
    else:
        account_list = Account.query.filter_by(account_owner=current_user).order_by(Account.date_opened.asc()).order_by(Account.date_closed.asc())

    return render_template(
        "main/accounts.html", title="Accounts", form=form, account_list=account_list
    )
    
    
@accounts.route("/account_info/<int:account_id>", methods=["GET", "POST"])
@login_required
def account_info(account_id):
    update_form = UpdateAccountForm()
    close_form = CloseAccountForm()
    csv_form = CSVUploadForm()
    account = Account.query.get_or_404(account_id)
    if account.account_owner != current_user:
        abort(404)
    elif request.method == "GET":
        update_form.account_name.data = account.account_name
        update_form.account_type.data = account.account_type
        update_form.date_opened.data = account.date_opened
        update_form.credit_limit.data = account.credit_limit
        update_form.benefit.data = account.benefit
        update_form.benefit_expiry.data = account.benefit_expiry
        update_form.notes.data = account.notes

    elif update_form.validate_on_submit():
        account.account_name = update_form.account_name.data
        account.account_type = update_form.account_type.data
        account.currency = update_form.currency.data.split()[0]
        account.date_opened = update_form.date_opened.data
        account.credit_limit = update_form.credit_limit.data
        account.benefit = update_form.benefit.data
        account.benefit_expiry = update_form.benefit_expiry.data
        account.pin = update_form.pin.data
        account.notes = update_form.notes.data
        db.session.commit()
        flash(f"Account updated", "success")
    
    elif close_form.validate_on_submit():
        account.date_closed = close_form.date_closed.data
        db.session.commit()
        flash(f"Account closed", "danger")

    elif csv_form.validate_on_submit():
        file = csv_form.file.data
        file.save(os.path.join(
            app.root_path,app.config["UPLOAD_FOLDER"],secure_filename(str(current_user.id)+"."+str(account_id)+"-"+file.filename)
            ))
        flash(f"File uploaded", "success")


    return render_template(
        "main/account_info.html",
        account=account,
        update_form=update_form,
        close_form=close_form,
        csv_form=csv_form,
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


@accounts.route("/account_info/<int:account_id>/reopen", methods=["GET", "POST"])
@login_required
def reopen_account(account_id):
    account = Account.query.get_or_404(account_id)
    if account.account_owner != current_user:
        abort(404)
    else:
        account.date_closed = None
        db.session.commit()
        return redirect(url_for("accounts.account_info", account_id=account.id))