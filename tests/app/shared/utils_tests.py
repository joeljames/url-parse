from nose.tools import assert_equal

from app.shared import utils


class TestForceString:

    def test_force_string_with_str(self):
        result = utils.force_str('abc')
        assert_equal(result, 'abc')

    def test_force_string_with_bytes(self):
        result = utils.force_str(b'abc')
        assert_equal(result, 'abc')
