from .forms import LoginForm, RegisterForm, TaskForm
from .db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, g


def save_task(form: TaskForm):
    db = get_db()

    db.execute(
        """INSERT INTO tasks (title, about, ends_on, author_id)
            VALUES (?, ?, ?, ?)""",
        (
            form.title.data,
            form.about.data,
            form.date.data,
            g.user['id']
        )
    )
    db.commit()


def create_user(form: RegisterForm):
    db = get_db()

    try:
        db.execute(
            """INSERT INTO user (username, password)
                VALUES (?, ?)""",
            (
                form.name.data,
                generate_password_hash(form.password.data)
            )
        )
        db.commit()
    except db.IntegrityError:
        error = f'User {form.name.data} is already registered.'
        return error


def log_in(form: LoginForm):
    db = get_db()
    error = None

    user = db.execute(
        """SELECT * FROM user WHERE username = ?""",
        (form.name.data,)
    ).fetchone()

    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], form.password.data):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']
    else:
        print(error)


def log_out():
    session.clear()


def get_user_tasks():
    db = get_db()
    tasks = db.execute(
        f"""SELECT title, about, created, ends_on, author_id, tasks.id
            FROM tasks JOIN user ON author_id={g.user['id']}
            GROUP BY tasks.id
            ORDER BY created ASC"""
    ).fetchall()

    return tasks


def delete_task(task_id):
    db = get_db()
    db.execute(
        f"""DELETE FROM tasks
            WHERE id={task_id} AND author_id={g.user['id']}"""
    )
    db.commit()
