from flask import (
    Blueprint,
    render_template
)
from .forms import RegisterForm, LoginForm

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('POST', 'GET'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/register.html', form=form)


@bp.route('/login', methods=('POST', 'GET'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/login.html', form=form)
