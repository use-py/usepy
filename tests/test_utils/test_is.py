from usepy import useIs


def test_is_token():
    assert useIs.token("token")
    assert not useIs.token("to")
    assert useIs.token("cd9bb741c5553b2243c6d39fb5dd3c34")


def test_is_regexp():
    import re
    assert not useIs.regexp("regex")
    assert not useIs.regexp(".*?")
    assert useIs.regexp(re.compile(".*?"))


def test_is_string():
    assert useIs.string("string")
    assert useIs.string(b"bytes")
    assert not useIs.string(123)
