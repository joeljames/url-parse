from nose.tools import (
    assert_equal,
    assert_true,
    assert_false
)
from mock import patch, DEFAULT, Mock

from app.factory import app_factory
from app.url_parsing.views import UrlParsingView


class TestUrlParsingView:

    def setUp(self):
        app_factory.app.config['TESTING'] = True
        app_factory.app.config['CSRF_ENABLED'] = False
        app_factory.app.config['WTF_CSRF_ENABLED'] = False
        self.app = app_factory.app
        self.test_client = self.app.test_client()

    @patch.object(UrlParsingView, 'repository_class')
    def test_get(self, repository_class):
        result = self.test_client.get('/')
        repository_class().get_list.assert_called_with(limit=5)
        assert_equal(result.status_code, 200)

    @patch.multiple('app.url_parsing.views',
                    UrlRequestForm=DEFAULT,
                    HtmlParser=DEFAULT)
    @patch.object(UrlParsingView, 'repository_class')
    def test_post(self,
                  repository_class,
                  UrlRequestForm,
                  HtmlParser):
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
        repository_class().create_or_incriment_count\
            .assert_called_with('http://kk.com')
        repository_class().get_list\
            .assert_called_with(limit=5)
        HtmlParser.assert_called_with()
        HtmlParser().feed.assert_called_with('http://kk.com')
        assert_equal(result.status_code, 200)

    @patch.multiple('app.url_parsing.views',
                    UrlRequestForm=DEFAULT,
                    HtmlParser=DEFAULT)
    @patch.object(UrlParsingView, 'repository_class')
    def test_invalid_post(self,
                          repository_class,
                          UrlRequestForm,
                          HtmlParser):
        UrlRequestForm.return_value.validate_on_submit.return_value = False
        result = self.test_client.post(
            '/',
            data=dict(
                url='http://kk.com'
            ),
            follow_redirects=True
        )
        assert_false(HtmlParser.called)
        repository_class().get_list\
            .assert_called_with(limit=5)
        assert_true('bg-danger' in str(result.data))
