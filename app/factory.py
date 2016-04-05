from flask import Flask

from app.url_parsing.urls import mod_url_parsing
from app.errors import add_error_handlers
from app.database import db
from app.shared.utils import get_config


__all__ = [
    'AppFactory',
    'app_factory',
]


class AppFactory(object):
    """
    It is called on the initial application start.
    The factory loads all the configuration defined in the `config.py`
    It also configures the db settings and views.
    """

    def __init__(self):
        self.app = Flask(
            __name__,
            static_folder=get_config('STATIC_FOLDER'),
            static_url_path=get_config('STATIC_URL_PATH'),
        )
        # Load config
        self.app.config.from_object('config')
        self.configure_db()
        self.configure_views()

    def configure_db(self):
        db.init_app(self.app)

    def configure_views(self):
        self.app.register_blueprint(mod_url_parsing)
        add_error_handlers(self.app)


app_factory = AppFactory()
