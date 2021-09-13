from flask import Flask, config
from flask_bootstrap import Bootstrap
from config import config_options
from .requests import configure_request
from .main import main as main_blueprint

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)


    app.register_blueprint(main_blueprint)

    configure_request(app)

    return app
