import pytest
from usepy.converter import to_list, to_md5, to_string, to_set, to_bool


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abc", ["a", "b", "c"]),
        ([1, 2, 3], [1, 2, 3]),
        ({"a": 1, "b": 2}, ["a", "b"]),
    ],
)
def test_to_list(input, expected):
    assert to_list(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("hello", "5d41402abc4b2a76b9719d911017c592"),
    ],
)
def test_to_md5(input, expected):
    assert to_md5(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (123, "123"),
        ([1, 2, 3], "1, 2, 3"),
        ({"a": 1, "b": 2}, "a: 1, b: 2"),
    ],
)
def test_to_string(input, expected):
    assert to_string(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, 2, 2, 3], {1, 2, 3}),
        ("hello", {"h", "e", "l", "o"}),
    ],
)
def test_to_set(input, expected):
    assert to_set(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, True),
        (0, False),
        ("true", True),
        ("false", False),
        ("", False),
        ("True", True),
        ("False", False),
        ("YES", True),
        ("NO", False),
        ("Y", True),
        ("N", False),
        ("1", True),
        ("0", False),
        ("yes", True),
        ("no", False),
        ("y", True),
    ],
)
def test_to_bool(input, expected):
    assert to_bool(input) == expected
