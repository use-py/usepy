from usepy import useIsRegexp, useIsString, useIsToken


def test_is_token():
    assert useIsToken("token")
    assert not useIsToken("to")
    assert useIsToken("cd9bb741c5553b2243c6d39fb5dd3c34")


def test_is_regexp():
    import re

    assert not useIsRegexp("regex")
    assert not useIsRegexp(".*?")
    assert useIsRegexp(re.compile(".*?"))


def test_is_string():
    assert useIsString("string")
    assert useIsString(b"bytes")
    assert not useIsString(123)
