from flask import Blueprint, render_template, redirect, url_for, g
from .forms import TaskForm
from .functions import save_task, get_user_tasks, delete_task


bp = Blueprint('tasks', __name__)


@bp.route('/', methods=('POST', 'GET'))
def index():
    try:
        tasks = get_user_tasks()
        form = TaskForm()
        if form.validate_on_submit():
            save_task(form)
            return redirect(url_for('tasks.index'))
    except BaseException:
        return redirect(url_for('auth.login'))

    return render_template('tasks/index.html', form=form, tasks=tasks)


@bp.route('/delete/<task_id>')
def del_task(task_id):
    if g.user is not None:
        delete_task(task_id)
        return redirect(url_for('tasks.index'))
    else:
        return redirect(url_for('auth.login'))
