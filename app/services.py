import sys
import logging


def configure_logger(app):
    out = logging.StreamHandler(sys.stdout)
    out.setLevel(logging.DEBUG)
    app.logger.addHandler(out)
    app.logger.setLevel(logging.DEBUG)


def configure_services(app):
    configure_logger(app)
