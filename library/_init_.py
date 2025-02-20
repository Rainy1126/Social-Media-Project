from flask import Flask
from .extension import db, ma
# import models
import os


def create_db(app):
    with app.app_context():
        if not os.path.exists("/library/library.db"):
            db.create_all()
            print("Database created")

# place imported blueprints here
blueprints = []

def create_app(config_file = "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    ma.init_app(app)
    db.init_app(app)
    create_db(app)
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    return app

