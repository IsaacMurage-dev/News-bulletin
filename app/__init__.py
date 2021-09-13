from flask import Flask, config
from flask_bootstrap import Bootstrap
from config import config_options
from .requests import configure_request
from .main import main as main_blueprint

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations.
    app.config.from_object(config_options[config_name])

    # Intitializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint

    app.register_blueprint(main_blueprint)

    # setting config
    configure_request(app)

    return app
