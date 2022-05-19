from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
        SECRET_KEY='ADJ@!*ÇOjas9s*C5lpK0!H@q#l&*1Kq*t4R#9DFI'
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import tasks
    app.register_blueprint(tasks.bp)

    return app
