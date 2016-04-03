from nose.tools import raises
from mock import patch, DEFAULT, Mock

from urllib.error import URLError
from wtforms.validators import ValidationError

from app.shared import validators


class TestUrlValidator:

    @patch.multiple('app.shared.validators',
                    urlopen=DEFAULT)
    def test_url_validator(self, urlopen):
        urlopen.return_value.getcode.return_value = 200
        field = Mock(name='field', data='http://foo.com')
        form = Mock(name='form')
        url_validator = validators.UrlValidator()
        url_validator(form, field)
        urlopen.assert_called_with('http://foo.com')
        urlopen().getcode.assert_called_with()

    @raises(ValidationError)
    @patch.multiple('app.shared.validators',
                    urlopen=DEFAULT)
    def test_url_validator_raises(self, urlopen):
        urlopen.side_effect = URLError
        field = Mock(name='field', data='http://foo.com')
        form = Mock(name='form')
        url_validator = validators.UrlValidator()
        url_validator(form, field)
