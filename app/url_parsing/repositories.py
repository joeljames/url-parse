from __future__ import absolute_import

from app.database import db
from app.url_parsing.models import UrlParseRequest


__all__ = [
    'UrlParseRequestRepository',
]


class UrlParseRequestRepository:
    """
    Repository interface for retrieving and managing url parse requests.
    """

    def __init__(self, query=None):
        self.query = query or UrlParseRequest.query

    def get_or_create(self, url):
        """
        Tries to get the url parse request object from the database.
        If the object does not exists it creates one.
        """
        created = False
        url_parse_request = self.get(url)
        if not url_parse_request:
            url_parse_request = self.create(
                url
            )
            created = True
        return url_parse_request, created

    def get(self, url):
        """
        Gets the url parse request object fom the database.
        Returns None if it soes not exist in the database.
        """
        return self.query.filter_by(url=url).first()

    def get_list(self, url=None, limit=None):
        """
        Retrives the url parse request objects from the db,
        based on the arguments passes in to filter the collection.
        """
        query = self.query.order_by(UrlParseRequest.count.desc())
        if url:
            query = query.filter_by(url=url)
        if limit:
            query = query.limit(limit)
        return query.all()

    def create(self, url, count=1):
        """
        Creates a url parse object and saves it to the db.
        """
        url_parse_request = UrlParseRequest(url, count)
        db.session.add(url_parse_request)
        db.session.commit()
        return url_parse_request

    def create_or_incriment_count(self, url):
        """
        Creates a url parse request object if it does not exist.
        Incriments the cont on the object it the already exist in the db.
        """
        obj, created = self.get_or_create(url)
        if not created:
            obj.count += 1
        db.session.commit()
        return obj

    def delete(self, url):
        """
        Deletes the url parse request object from the db.
        """
        obj = self.get(url)
        db.session.delete(obj)
        db.session.commit()
