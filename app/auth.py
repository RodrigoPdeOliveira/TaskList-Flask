from .forms import RegisterForm, LoginForm, NewPassword, NewUsername
from .functions import (
    change_password, create_user, delete_account, delete_all_tasks, log_in,
    log_out, check_password_hash, change_username
    )
from .db import get_db
from flask import Blueprint, render_template, redirect, url_for, g, session


bp = Blueprint('auth', __name__)


@bp.route('/register', methods=('POST', 'GET'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user(form)
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@bp.route('/login', methods=('POST', 'GET'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        log_in(form)
        return redirect(url_for('tasks.index'))

    return render_template('auth/login.html', form=form)


@bp.route('/user', methods=('POST', 'GET'))
def user():
    if g.user is not None:
        new_pw = NewPassword()
        if new_pw.validate_on_submit():
            if check_password_hash(
                g.user['password'],
                new_pw.old_password.data
                    ):
                change_password(new_pw.new_password.data)
                return redirect(url_for('auth.user'))

        new_usrnm = NewUsername()
        if new_usrnm.validate_on_submit():
            if check_password_hash(
                g.user['password'],
                new_usrnm.password.data
                    ):
                change_username(new_usrnm.new_username.data)
                return redirect(url_for('auth.user'))

        return render_template(
            'auth/user.html', password=new_pw, username=new_usrnm
            )
    else:
        return redirect(url_for('auth.login'))


@bp.route('/logout')
def logout():
    log_out()
    return redirect(url_for('auth.login'))


@bp.route('/delete_tasks')
def del_tasks():
    if g.user is not None:
        delete_all_tasks()
        return redirect(url_for('auth.user'))
    else:
        return redirect(url_for('auth.login'))


@bp.route('/delete_account')
def del_account():
    if g.user is not None:
        delete_account()
        session.clear()
    return redirect(url_for('auth.login'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            """SELECT * FROM user WHERE id = ?""",
            (user_id,)
        ).fetchone()
