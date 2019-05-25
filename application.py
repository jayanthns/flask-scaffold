import os

from flask import Flask

from flask_migrate import MigrateCommand
from extensions import (
    bcrypt,
    db,
    migrate,
    ma
)
import logging.config

# models import
from models.article import *

from app.article.views import article_api_blueprint

SETTINGS_FILE = os.environ.get("FLASK_ENV", "settings.dev_settings")


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    # cache.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    # redis_store.init_app(app)
    logging.config.dictConfig(app.config["LOGGING"])
    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    # app.register_blueprint(public.views.blueprint)
    app.register_blueprint(article_api_blueprint, url_prefix="/api/articles")
    return app


def create_app(config_object='settings.base_settings'):
    """Creating the app instance function

    Keyword Arguments:
        config_object {settings} -- [description] (default: {'settings.base_settings'})
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config.from_object(SETTINGS_FILE)
    register_extensions(app)
    register_blueprints(app)
    return app
