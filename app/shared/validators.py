from urllib.request import urlopen
from urllib.error import URLError

from wtforms.validators import ValidationError

from app.shared.services import get_logger


__all__ = [
    'UrlValidator'
]


class UrlValidator:
    """
    Validator to check if the URL is reachable.
    Tries to make a request to the URL, if the
    request fails the exception is caught and logged.
    """

    def __init__(self,
                 message='This URL is not rechable.',
                 logger=None):
        self.message = message
        self.logger = logger or get_logger('url_validator')

    def __call__(self, form, field):
        code = 0
        try:
            code = urlopen(field.data).getcode()
        except URLError as e:
            if hasattr(e, 'reason'):
                self.logger.error('Failed to reach the server.')
                self.logger.error('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                self.logger.error(
                    'The server was unable to complete the request.'
                )
                self.logger.error('Error code: ', e.code)
        finally:
            if code != 200:
                raise ValidationError(self.message)
