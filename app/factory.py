from flask import Flask

from app.url_parsing.urls import mod_url_parsing
from app.services import configure_services
from app.errors import add_error_handlers
from app.database import db


__all__ = [
    'AppFactory',
    'app_factory',
]


class AppFactory(object):

    def __init__(self):
        self.app = Flask(
            __name__,
        )
        # Load config
        self.app.config.from_object('config')
        configure_services(self.app)
        self.configure_db()
        self.configure_views()

    def configure_db(self):
        db.init_app(self.app)

    def configure_views(self):
        self.app.register_blueprint(mod_url_parsing)
        add_error_handlers(self.app)


app_factory = AppFactory()
