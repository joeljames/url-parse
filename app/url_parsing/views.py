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
from app.shared.mixins import RepositoryMixin


__all__ = [
    'UrlParsingView',
]


class UrlParsingView(MethodView,
                     RepositoryMixin):
    """
    The URL parsing view.
    The routing for this view is defined in `url.py`.
    """

    repository_class = UrlParseRequestRepository

    def __init__(self,
                 logger=None,
                 template_name='index.html'):
        super().__init__()
        self.template_name = template_name
        self.logger = logger or get_logger('views')

    def get(self):
        """
        Handles the GET request.
        Renders the from and URL parse request history.
        The request history is limited to top 5 most pasred URLs
        """
        form = UrlRequestForm(request.form)
        url_parse_requests = self.repository.get_list(limit=5)
        return render_template(
            self.template_name,
            form=form,
            url_parse_requests=url_parse_requests
        )

    def post(self):
        """
        Handles the POST when a user fills in the URLRequestForm
        and hits submit.
        If the form is valid ie: a valid URL is submitted, then the
        requested url is sent to the `HtmlParser` which parses and
        returns the summary (tag count),
        It also logs any from error if the user submits an invalid request.
        """
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
