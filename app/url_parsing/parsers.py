from html.parser import HTMLParser
from collections import defaultdict
from urllib.request import urlopen

from app.shared.utils import force_str
from app.shared.services import get_logger


__all__ = [
    'HtmlParser',
]


class HtmlParser(HTMLParser):
    """
    Simple Html parser.
    """
    summary_dict = defaultdict(int)
    errror_list = []

    def __init__(self, *args, **kwargs):
        self.logger = (
            kwargs.pop('logger', None) or
            get_logger('html_parser')
        )
        super().__init__(*args, **kwargs)

    def feed(self, url):
        try:
            response = urlopen(url)
            self._data = force_str(response.read())
            super().feed(self._data)
        except Exception as e:
            self.errror_list.append(e)
            self.logger.exception(e)

    @property
    def summary(self):
        return self.summary_dict

    @property
    def errros(self):
        return self.errror_list

    @property
    def is_successfull(self):
        return len(self.errror_list) == 0

    @property
    def data(self):
        return self._data

    def reset(self):
        self._data = None
        self.summary_dict = defaultdict(int)
        super().reset()

    def handle_starttag(self, tag, attrs):
        self.summary_dict[tag] += 1

    def handle_endtag(self, tag):
        self.summary_dict[tag] += 1
