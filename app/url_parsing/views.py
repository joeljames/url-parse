from __future__ import absolute_import

from flask.views import MethodView
from flask import render_template


__all__ = [
    'UrlParsingView'
]


class UrlParsingView(MethodView):

    def get(self):
        return render_template(
            'index.html'
        )
