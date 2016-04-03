from functools import partial

from flask import render_template


__all__ = [
    'add_error_handlers'
]


def not_found(error):
    return render_template('404.html'), 404


def server_error(error, app=None):
    app.logger.exception(error)
    return render_template('500.html'), 500


def add_error_handlers(app):
    app.error_handler_spec[None][404] = not_found
    app.error_handler_spec[None][500] = partial(server_error, app=app)
