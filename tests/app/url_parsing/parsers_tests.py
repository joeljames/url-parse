from nose.tools import (
    assert_equal,
    assert_is_none,
    assert_true
)
from mock import patch, DEFAULT

from collections import defaultdict
from app.url_parsing import parsers


class TestHtmlParser:

    def setUp(self):
        self.url = 'http://foo.com'

    @patch.multiple('app.url_parsing.parsers',
                    urlopen=DEFAULT,
                    force_str=DEFAULT)
    def test_feed(self, urlopen, force_str):
        parsers.HtmlParser().feed(self.url)
        urlopen.assert_called_with(self.url)
        force_str.assert_called_with(urlopen().read())

    @patch.multiple('app.url_parsing.parsers',
                    urlopen=DEFAULT,
                    force_str=DEFAULT)
    def test_summary(self, urlopen, force_str):
        force_str.return_value = '<html></html>'
        p = parsers.HtmlParser()
        p.feed(self.url)
        assert_equal(p.summary['html'], 2)

    @patch.multiple('app.url_parsing.parsers',
                    urlopen=DEFAULT,
                    force_str=DEFAULT)
    def test_is_successfull(self, urlopen, force_str):
        force_str.return_value = '<html></html>'
        p = parsers.HtmlParser()
        p.feed(self.url)
        assert_true(p.is_successfull)

    @patch.multiple('app.url_parsing.parsers',
                    urlopen=DEFAULT,
                    force_str=DEFAULT)
    def test_data(self, urlopen, force_str):
        force_str.return_value = '<html></html>'
        p = parsers.HtmlParser()
        p.feed(self.url)
        assert_equal(p.data, '<html></html>')

    @patch.multiple('app.url_parsing.parsers',
                    urlopen=DEFAULT,
                    force_str=DEFAULT)
    def test_reset(self, urlopen, force_str):
        force_str.return_value = '<html></html>'
        p = parsers.HtmlParser()
        p.feed(self.url)
        p.reset()
        assert_is_none(p.data)
        assert_equal(p.summary, defaultdict(int))
