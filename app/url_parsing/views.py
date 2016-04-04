from __future__ import absolute_import

from flask.views import MethodView
from flask import (
    render_template,
    request
)

from app.url_parsing.forms import UrlRequestForm
from app.url_parsing.parsers import HtmlParser
from app.shared.services import get_logger
from app.url_parsing.repositories import UrlParseRequestRepository


__all__ = [
    'UrlParsingView'
]


class UrlParsingView(MethodView):

    def __init__(self,
                 logger=None,
                 repository=None,
                 template_name='index.html'):
        super().__init__()
        self.repository = repository or UrlParseRequestRepository()
        self.template_name = template_name
        self.logger = logger or get_logger('views')

    def get(self):
        form = UrlRequestForm(request.form)
        url_parse_requests = self.repository.get_list(limit=5)
        return render_template(
            self.template_name,
            form=form,
            url_parse_requests=url_parse_requests
        )

    def post(self):
        parser = None
        form = UrlRequestForm(request.form)
        if form.validate_on_submit():
            parser = HtmlParser()
            parser.feed(form.url.data)
            if parser.is_successfull:
                self.repository\
                    .create_or_incriment_count(form.url.data)
        else:
            self.logger.error(form.errors)
        url_parse_requests = self.repository.get_list(limit=5)
        return render_template(
            self.template_name,
            form=form,
            parser=parser,
            url_parse_requests=url_parse_requests
        )
