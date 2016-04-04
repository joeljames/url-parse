from mock import patch, DEFAULT

import tasks


class TestCreateDb:

    @patch.multiple('tasks',
                    db=DEFAULT)
    def test_create_db(self, db):
        tasks.create_db()
        db.create_all.assert_called_with()

    @patch.multiple('tasks',
                    db=DEFAULT)
    def test_drop_db(self, db):
        tasks.drop_db()
        db.drop_all.assert_called_with()

    @patch.multiple('tasks',
                    create_db=DEFAULT,
                    drop_db=DEFAULT)
    def test_rebuild_db(self, create_db, drop_db):
        tasks.rebuild_db()
        drop_db.assert_called_with()
        create_db.assert_called_with()
