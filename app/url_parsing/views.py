from __future__ import absolute_import

from flask.views import MethodView
from flask import (
    render_template,
    request
)

from app.url_parsing.forms import UrlRequestForm
from app.url_parsing.parsers import HtmlParser
from app.shared.services import get_logger


__all__ = [
    'UrlParsingView'
]


class UrlParsingView(MethodView):

    def __init__(self,
                 logger=None,
                 template_name='index.html'):
        super().__init__()
        self.template_name = template_name
        self.logger = logger or get_logger('views')

    def get(self):
        form = UrlRequestForm(request.form)
        return render_template(
            self.template_name,
            form=form
        )

    def post(self):
        parser = None
        form = UrlRequestForm(request.form)
        if form.validate_on_submit():
            parser = HtmlParser()
            parser.feed(form.url.data)
        else:
            self.logger.error(form.errors)
        return render_template(
            self.template_name,
            form=form,
            parser=parser
        )
