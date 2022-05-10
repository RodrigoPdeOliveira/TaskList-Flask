from flask import Blueprint, render_template, redirect, url_for
from .forms import TaskForm
from .functions import save_task, get_user_tasks


bp = Blueprint('tasks', __name__)


@bp.route('/', methods=('POST', 'GET'))
def index():
    tasks = get_user_tasks()
    form = TaskForm()
    if form.validate_on_submit():
        save_task(form)
        return redirect(url_for('tasks.index'))
    return render_template('tasks/index.html', form=form, tasks=tasks)
