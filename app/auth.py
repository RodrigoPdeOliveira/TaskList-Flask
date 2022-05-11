from .forms import RegisterForm, LoginForm
from .functions import create_user, log_in, log_out
from .db import get_db
from flask import Blueprint, render_template, redirect, url_for, g, session


bp = Blueprint('auth', __name__, url_prefix='/auth')


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


@bp.route('/logout')
def logout():
    log_out()
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
