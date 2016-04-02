from urllib.request import urlopen
from urllib.error import URLError

from wtforms.validators import ValidationError


__all__ = [
    'UrlValidator'
]


class UrlValidator:
    """
    Validator to check if the URL is reachable.
    """

    def __init__(self,
                 message='This URL is not rechable.'):
        self.message = message

    def __call__(self, form, field):
        try:
            code = urlopen(field.data).getcode()
        except URLError:
            code = 0
        finally:
            if code != 200:
                raise ValidationError(self.message)