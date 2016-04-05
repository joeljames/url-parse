from flask_wtf import Form
from wtforms import validators
from wtforms.fields.html5 import URLField

from app.shared.validators import UrlValidator


__all__ = [
    'UrlRequestForm',
]


class UrlRequestForm(Form):
    """
    The URL parse request form.
    Also, takes care of the validations on the URL field.
    """

    url = URLField(
        'URL',
        [
            validators.url(),
            validators.Required(message='Must provide a valid web url.'),
            UrlValidator()
        ]
    )
