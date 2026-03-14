import pytest
from usepy.validator import is_empty, is_email, is_json, is_number


class TestIsEmpty:
    """Tests for is_empty() function"""

    def test_is_empty_none(self):
        assert is_empty(None) is True

    def test_is_empty_string(self):
        assert is_empty('') is True
        assert is_empty('   ') is True

    def test_is_empty_list(self):
        assert is_empty([]) is True

    def test_is_empty_tuple(self):
        assert is_empty(()) is True

    def test_is_empty_dict(self):
        assert is_empty({}) is True

    def test_is_empty_set(self):
        assert is_empty(set()) is True

    def test_is_empty_zero(self):
        assert is_empty(0) is True
        assert is_empty(0.0) is True
        assert is_empty(False) is True

    def test_is_not_empty_string(self):
        assert is_empty('hello') is False

    def test_is_not_empty_list(self):
        assert is_empty([1]) is False

    def test_is_not_empty_dict(self):
        assert is_empty({'a': 1}) is False


class TestIsEmail:
    """Tests for is_email() function"""

    def test_valid_email(self):
        assert is_email('user@example.com') is True
        assert is_email('user.name@domain.co.uk') is True
        assert is_email('test+tag@gmail.com') is True

    def test_invalid_email(self):
        assert is_email('invalid.email') is False
        assert is_email('user@') is False
        assert is_email('@example.com') is False
        assert is_email('user@domain') is False

    def test_empty_email(self):
        assert is_email('') is False
        assert is_email(None) is False


class TestIsJson:
    """Tests for is_json() function"""

    def test_valid_json(self):
        assert is_json('{"key": "value"}') is True
        assert is_json('{"nested": {"key": [1, 2, 3]}}') is True
        assert is_json('[1, 2, 3]') is True
        assert is_json('null') is True
        assert is_json('true') is True
        assert is_json('"string"') is True
        assert is_json('123') is True
        assert is_json('null') is True

    def test_invalid_json(self):
        assert is_json('{"invalid": value}') is False
        assert is_json('not json') is False
        assert is_json('{') is False
        assert is_json('') is False  # Empty string is NOT valid JSON

    def test_none_is_json(self):
        assert is_json(None) is False


class TestIsNumber:
    """Tests for is_number() function"""

    def test_int_is_number(self):
        assert is_number(123) is True
        assert is_number(-456) is True

    def test_float_is_number(self):
        assert is_number(123.45) is True
        assert is_number(-78.9) is True

    def test_numeric_string_is_number(self):
        assert is_number('123') is True
        assert is_number('123.45') is True
        assert is_number('-123') is True

    def test_non_numeric_string_not_number(self):
        assert is_number('abc') is False
        assert is_number('12a34') is False
        assert is_number('hello') is False

    def test_zero_is_number(self):
        assert is_number(0) is True
        assert is_number(0.0) is True

    def test_none_not_number(self):
        assert is_number(None) is False

    def test_empty_string_not_number(self):
        assert is_number('') is False

    def test_whitespace_not_number(self):
        assert is_number('   ') is False