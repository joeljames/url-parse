from __future__ import absolute_import
from app.database import db


__all__ = [
    'UrlParseRequest',
]


class UrlParseRequest(db.Model):
    """
    The database model for `url_parse_request` model.
    """

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, url, count):
        self.url = url
        self.count = count

    def __repr__(self):
        return '<UrlParseRequest %r: %r>' % (self.url, self.count)
