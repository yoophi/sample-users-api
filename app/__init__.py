from flask import Flask

from app.api import api


def init_blueprints(app):
    app.register_blueprint(api)


def create_app():
    app = Flask(__name__)
    init_blueprints(app)
    return app
