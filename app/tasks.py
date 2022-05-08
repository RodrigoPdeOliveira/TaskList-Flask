from flask import (
    Blueprint,
    render_template
)
from .forms import TaskForm


bp = Blueprint('tasks', __name__)


@bp.route('/', methods=('POST', 'GET'))
def index():
    form = TaskForm()
    if form.validate_on_submit():
        pass
    return render_template('tasks/index.html', form=form)
