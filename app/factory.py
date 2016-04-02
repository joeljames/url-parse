from flask import Flask

from app.url_parsing.urls import mod_url_parsing
from app.services import configure_services


__all__ = [
    'AppFactory'
]


class AppFactory(object):

    def __init__(self):
        self.app = Flask(
            __name__,
        )
        # Load config
        self.app.config.from_object('config')
        configure_services(self.app)
        self.configure_views()

    def configure_views(self):
        self.app.register_blueprint(mod_url_parsing)
