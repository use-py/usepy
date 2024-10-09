import pytest
from usepy.string import (
    camel_case,
    capitalize,
    kebab_case,
    left,
    lower_case,
    middle,
    middle_batch,
    pascal_case,
    right,
    snake_case,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        ("hello world", "helloWorld"),
        ("foo_bar", "fooBar"),
    ],
)
def test_camel_case(input, expected):
    assert camel_case(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("hello", "Hello"),
        ("WORLD", "World"),
    ],
)
def test_capitalize(input, expected):
    assert capitalize(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("hello world", "hello-world"),
        ("fooBar", "foo-bar"),
    ],
)
def test_kebab_case(input, expected):
    assert kebab_case(input) == expected


@pytest.mark.parametrize(
    "input, end, expected",
    [
        ("hello", "lo", "hel"),
        ("python", "on", "pyth"),
    ],
)
def test_left(input, end, expected):
    assert left(input, end) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("HELLO", "hello"),
        ("World", "world"),
    ],
)
def test_lower_case(input, expected):
    assert lower_case(input) == expected


@pytest.mark.parametrize(
    "input, start, end, expected",
    [
        ("python", "py", "on", "th"),
        ("hello", "hel", "o", "l"),
    ],
)
def test_middle(input, start, end, expected):
    assert middle(input, start, end) == expected


@pytest.mark.parametrize(
    "input, start, end, expected",
    [
        ("a1b2a3b4a", "a", "b", ["1", "3"]),
    ],
)
def test_middle_batch(input, start, end, expected):
    assert middle_batch(input, start, end) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("hello world", "HelloWorld"),
        ("foo_bar", "FooBar"),
    ],
)
def test_pascal_case(input, expected):
    assert pascal_case(input) == expected


@pytest.mark.parametrize(
    "input, end, expected",
    [
        ("hello", "l", "lo"),
        ("python", "th", "on"),
    ],
)
def test_right(input, end, expected):
    assert right(input, end) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("helloWorld", "hello_world"),
        ("foo-bar", "foo_bar"),
    ],
)
def test_snake_case(input, expected):
    assert snake_case(input) == expected
