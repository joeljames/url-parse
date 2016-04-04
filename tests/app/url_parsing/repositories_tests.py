from nose.tools import (
    assert_equal,
    assert_true,
    assert_false
)
from mock import Mock, patch, DEFAULT

from app.url_parsing.repositories import (
    UrlParseRequestRepository
)


class TestUrlParseRequestRepository:

    def setUp(self):
        self.url = 'http://kk.com'
        self.query = Mock(name='query')
        self.repository = UrlParseRequestRepository(
            query=self.query
        )

    @patch.object(UrlParseRequestRepository, 'create')
    @patch.object(UrlParseRequestRepository, 'get')
    def test_get_or_create_without_create(self, get, create):
        obj, created_status = self.repository.get_or_create(self.url)
        get.assert_called_with(self.url)
        assert_false(create.called)
        assert_false(created_status)

    @patch.object(UrlParseRequestRepository, 'create')
    @patch.object(UrlParseRequestRepository, 'get')
    def test_get_or_create_with_create(self, get, create):
        get.return_value = None
        obj, created_status = self.repository.get_or_create(self.url)
        get.assert_called_with(self.url)
        create.assert_called_with(self.url)
        assert_true(created_status)

    def test_get(self):
        self.repository.get(self.url)
        self.query.filter_by.assert_called_with(
            url=self.url
        )
        self.query.filter_by().first.assert_called_with()

    @patch.multiple('app.url_parsing.repositories',
                    UrlParseRequest=DEFAULT)
    def test_get_list(self, UrlParseRequest):
        self.repository.get_list(url=self.url, limit=5)
        self.query.order_by.assert_called_with(
            UrlParseRequest.count.desc()
        )
        self.query.order_by().filter_by.assert_called_with(
            url=self.url
        )
        self.query.order_by().filter_by().limit.assert_called_with(5)
        self.query.order_by().filter_by().limit().all.assert_called_with()

    @patch.multiple('app.url_parsing.repositories',
                    UrlParseRequest=DEFAULT,
                    db=DEFAULT)
    def test_create(self, UrlParseRequest, db):
        self.repository.create(url=self.url)
        UrlParseRequest.assert_called_with(self.url, 1)
        db.session.add.assert_called_with(UrlParseRequest())
        db.session.commit.assert_called_with()

    @patch.object(UrlParseRequestRepository, 'get_or_create')
    @patch.multiple('app.url_parsing.repositories',
                    db=DEFAULT)
    def test_create_or_incriment_count_with_create(self, get_or_create, db):
        get_or_create.return_value = (Mock(name='obj', count=1), True)
        obj = self.repository.create_or_incriment_count(url=self.url)
        get_or_create.assert_called_with(self.url)
        db.session.commit.assert_called_with()
        assert_equal(obj.count, 1)

    @patch.object(UrlParseRequestRepository, 'get_or_create')
    @patch.multiple('app.url_parsing.repositories',
                    db=DEFAULT)
    def test_create_or_incriment_count_without_create(self, get_or_create, db):
        get_or_create.return_value = (Mock(name='obj', count=5), False)
        obj = self.repository.create_or_incriment_count(url=self.url)
        get_or_create.assert_called_with(self.url)
        db.session.commit.assert_called_with()
        assert_equal(obj.count, 6)

    @patch.object(UrlParseRequestRepository, 'get')
    @patch.multiple('app.url_parsing.repositories',
                    db=DEFAULT)
    def test_delete(self, get, db):
        obj = Mock(name='obj')
        get.return_value = obj
        self.repository.delete(self.url)
        get.assert_called_with(self.url)
        db.session.delete.assert_called_with(obj)
        db.session.commit.assert_called_with()
