from html.parser import HTMLParser
from collections import defaultdict
from urllib.request import urlopen

from app.shared.utils import force_str


__all__ = [
    'HtmlParser',
]


class HtmlParser(HTMLParser):
    """
    Simple Html parser.
    """
    summary_dict = defaultdict(int)

    def feed(self, url):
        response = urlopen(url)
        self._data = force_str(response.read())
        super().feed(self._data)

    @property
    def summary(self):
        return self.summary_dict

    @property
    def data(self):
        return self._data

    def reset(self):
        self._raw_source = None
        self.summary_dict = defaultdict(int)
        super().reset()

    def handle_starttag(self, tag, attrs):
        self.summary_dict[tag] += 1

    def handle_endtag(self, tag):
        self.summary_dict[tag] += 1
