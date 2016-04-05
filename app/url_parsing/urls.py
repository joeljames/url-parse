"""
This module handles the routing to the server.
Based on the URL requested, the router will call out to the
respective view.
"""

from __future__ import absolute_import
from flask import Blueprint

from app.url_parsing.views import (
    UrlParsingView,
)


__all__ = [
    'mod_url_parsing'
]

# Instantiates the BluePrint
mod_url_parsing = Blueprint(
    'url_parsing',
    __name__,
    url_prefix='/'
)

# Add the routing. Calls the `UrlParsingView` whe the user access the root
mod_url_parsing.add_url_rule(
    '/',
    view_func=UrlParsingView.as_view('url_parsing_detail')
)
