from nose.tools import assert_equal, assert_true
from mock import patch, DEFAULT, Mock

from app.factory import app_factory


class TestUrlParsingView:

    def setUp(self):
        app_factory.app.config['TESTING'] = True
        app_factory.app.config['CSRF_ENABLED'] = False
        app_factory.app.config['WTF_CSRF_ENABLED'] = False
        self.app = app_factory.app
        self.test_client = self.app.test_client()

    def test_get(self):
        result = self.test_client.get('/')
        assert_equal(result.status_code, 200)

    @patch.multiple('app.url_parsing.views',
                    UrlRequestForm=DEFAULT,
                    HtmlParser=DEFAULT)
    def test_post(self, UrlRequestForm, HtmlParser):
        UrlRequestForm.return_value = Mock(
            name='form',
            url=Mock(name='url', data='http://kk.com')
        )
        UrlRequestForm.return_value.validate_on_submit.return_value = True
        result = self.test_client.post(
            '/',
            data=dict(
                url='http://kk.com'
            ),
            follow_redirects=True
        )
        HtmlParser.assert_called_with()
        HtmlParser().feed.assert_called_with('http://kk.com')
        assert_equal(result.status_code, 200)

    @patch.multiple('app.url_parsing.views',
                    UrlRequestForm=DEFAULT)
    def test_invalid_post(self, UrlRequestForm):
        UrlRequestForm.return_value.validate_on_submit.return_value = False
        result = self.test_client.post(
            '/',
            data=dict(
                url='http://kk.com'
            ),
            follow_redirects=True
        )
        assert_true('bg-danger' in str(result.data))
