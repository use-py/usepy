from usepy import useIs


def test_is_token():
    assert useIs.is_token("token")
    assert not useIs.is_token("to")
    assert useIs.is_token("cd9bb741c5553b2243c6d39fb5dd3c34")


def test_is_regexp():
    import re
    assert not useIs.is_regexp("regex")
    assert not useIs.is_regexp(".*?")
    assert useIs.is_regexp(re.compile(".*?"))


def test_is_string():
    assert useIs.is_string("string")
    assert useIs.is_string(b"bytes")
    assert not useIs.is_string(123)
