import pytest
from usepy.converter import to_list, to_md5, to_string, to_set, to_bool


class TestToList:
    """Tests for to_list() function"""

    @pytest.mark.parametrize(
        "input, expected",
        [
            ("abc", ["a", "b", "c"]),
            ([1, 2, 3], [1, 2, 3]),
            ({"a": 1, "b": 2}, ["a", "b"]),
            ((1, 2, 3), [1, 2, 3]),
            ({1, 2, 3}, list({1, 2, 3})),
        ],
    )
    def test_to_list_normal(self, input, expected):
        result = to_list(input)
        if isinstance(expected, list) and isinstance(input, set):
            assert set(result) == set(expected)
        else:
            assert result == expected

    def test_to_list_none(self):
        """Test to_list with None returns empty list"""
        assert to_list(None) == []

    def test_to_list_single_value(self):
        """Test to_list with single non-iterable value"""
        assert to_list(123) == [123]

    def test_to_list_bytes(self):
        """Test to_list with bytes returns list of integers"""
        assert to_list(b"abc") == [97, 98, 99]


class TestToMd5:
    """Tests for to_md5() function"""

    def test_to_md5_string(self):
        """Test to_md5 with string"""
        assert to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    def test_to_md5_bytes(self):
        """Test to_md5 with bytes"""
        assert to_md5(b"hello") == "5d41402abc4b2a76b9719d911017c592"

    def test_to_md5_empty_string(self):
        """Test to_md5 with empty string"""
        assert to_md5("") == "d41d8cd98f00b204e9800998ecf8427e"

    def test_to_md5_number(self):
        """Test to_md5 with number"""
        assert to_md5(123) == "202cb962ac59075b964b07152d234b70"

    def test_to_md5_none(self):
        """Test to_md5 with None"""
        assert to_md5(None) == "d41d8cd98f00b204e9800998ecf8427e"


class TestToString:
    """Tests for to_string() function"""

    @pytest.mark.parametrize(
        "input, expected",
        [
            (123, "123"),
            ([1, 2, 3], "1, 2, 3"),
            ({"a": 1, "b": 2}, "a: 1, b: 2"),
            ((1, 2, 3), "1, 2, 3"),
            ({1, 2, 3}, "1, 2, 3"),
        ],
    )
    def test_to_string_normal(self, input, expected):
        # For set, order is not guaranteed
        result = to_string(input)
        if isinstance(input, set):
            assert set(result.split(", ")) == set(expected.split(", "))
        else:
            assert result == expected

    def test_to_string_none(self):
        """Test to_string with None returns empty string"""
        assert to_string(None) == ""

    def test_to_string_bytes(self):
        """Test to_string with bytes decodes to utf-8"""
        assert to_string(b"hello") == "hello"

    def test_to_string_empty_list(self):
        """Test to_string with empty list"""
        assert to_string([]) == ""

    def test_to_string_empty_dict(self):
        """Test to_string with empty dict"""
        assert to_string({}) == ""


class TestToSet:
    """Tests for to_set() function"""

    @pytest.mark.parametrize(
        "input, expected",
        [
            ([1, 2, 2, 3], {1, 2, 3}),
            ("hello", {"h", "e", "l", "o"}),
            ((1, 2, 2, 3), {1, 2, 3}),
            ({1, 2, 3}, {1, 2, 3}),
        ],
    )
    def test_to_set_normal(self, input, expected):
        assert to_set(input) == expected

    def test_to_set_none(self):
        """Test to_set with None returns empty set"""
        assert to_set(None) == set()

    def test_to_set_empty_list(self):
        """Test to_set with empty list"""
        assert to_set([]) == set()


class TestToBool:
    """Tests for to_bool() function"""

    @pytest.mark.parametrize(
        "input, expected",
        [
            # Boolean values
            (True, True),
            (False, False),
            # Integer values
            (1, True),
            (0, False),
            (-1, True),
            # Float values
            (1.0, True),
            (0.0, False),
            # String: true/false variants
            ("true", True),
            ("false", False),
            ("True", True),
            ("False", False),
            ("TRUE", True),
            ("FALSE", False),
            # String: yes/no variants
            ("yes", True),
            ("no", False),
            ("YES", True),
            ("NO", False),
            ("Y", True),
            ("N", False),
            ("y", True),
            ("n", False),
            # String: t/f variants
            ("t", True),
            ("f", False),
            ("T", True),
            ("F", False),
            # String: on/off/enabled/disabled
            ("on", True),
            ("enabled", True),
            # String: numeric
            ("1", True),
            ("0", False),
        ],
    )
    def test_to_bool_normal(self, input, expected):
        assert to_bool(input) == expected

    def test_to_bool_none(self):
        """Test to_bool with None returns False"""
        assert to_bool(None) is False

    def test_to_bool_empty_string(self):
        """Test to_bool with empty string returns False"""
        assert to_bool("") is False

    def test_to_bool_whitespace_string(self):
        """Test to_bool with whitespace-only string returns False"""
        assert to_bool("   ") is False

    def test_to_bool_other_string(self):
        """Test to_bool with other string returns False"""
        assert to_bool("random") is False

    def test_to_bool_list(self):
        """Test to_bool with non-empty list returns True"""
        assert to_bool([1, 2]) is True

    def test_to_bool_empty_list(self):
        """Test to_bool with empty list returns False"""
        assert to_bool([]) is False