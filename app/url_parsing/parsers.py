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
        """
        Fetches the URL and passes the source data in to HTMLParser.feed
        Also, catches any exception raised and logs the exception and
        appends the error to the errror_list.
        """
        try:
            response = urlopen(url)
            self._data = force_str(response.read())
            super().feed(self._data)
        except Exception as e:
            self.errror_list.append(e)
            self.logger.exception(e)

    @property
    def summary(self):
        """
        Returns the summary dict which contains counts of
        start tag and end tag.
        eg: {'html', 2}
        """
        return self.summary_dict

    @property
    def errros(self):
        """
        Returns a list of errors that occured while trying to
        fetch the url and parse the url.
        """
        return self.errror_list

    @property
    def is_successfull(self):
        """
        Returns True if the parse was successfull else False.
        """
        return len(self.errror_list) == 0

    @property
    def data(self):
        """
        Returns the raw fetched data from the URL.
        """
        return self._data

    def reset(self):
        """
        Resets the parser.
        """
        self._data = None
        self.summary_dict = defaultdict(int)
        super().reset()

    def handle_starttag(self, tag, attrs):
        """
        Handles the start tag.
        Increments the cont of the tag on the summary_dict.
        """
        self.summary_dict[tag] += 1

    def handle_endtag(self, tag):
        """
        Handles the end tag.
        Increments the cont of the tag on the summary_dict.
        """
        self.summary_dict[tag] += 1
