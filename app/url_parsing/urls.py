from __future__ import absolute_import
from flask import Blueprint

from app.url_parsing.views import (
    UrlParsingView,
)


__all__ = [
    'mod_url_parsing'
]


mod_url_parsing = Blueprint(
    'url-parsing',
    __name__,
    url_prefix='/'
)

mod_url_parsing.add_url_rule(
    '/',
    view_func=UrlParsingView.as_view('url-parse-detail')
)
