from flask_wtf import Form
from wtforms import validators
from wtforms.fields.html5 import URLField


__all__ = [
    'UrlRequestForm',
]


class UrlRequestForm(Form):

    url = URLField(
        'URL',
        [
            validators.url(),
            validators.Required(message='Must provide a valid web url.')
        ]
    )
