from usepy import useStringLeft, useStringMiddle, useStringMiddleBatch, useStringRight


def test_get_middle():
    assert useStringMiddle("abc123def", "abc", "def") == "123"
    assert useStringMiddle("abc123def", "abc") == "123def"
    assert useStringMiddle("abc123def", end_str="def") == "abc123"


def test_get_middle_batch():
    assert useStringMiddleBatch("abc123def456abc789def", "abc", "def") == ["123", "789"]
    assert useStringMiddleBatch("abc123def456abc789def", "abc", "def", 1) == ["123"]
    assert useStringMiddleBatch("abc123def456abc789def", end_str="def") == [
        "abc123",
        "456abc789",
    ]
    assert useStringMiddleBatch("abc123def456abc789def", start_str="abc") == [
        "123def456abc789def"
    ]


def test_get_left():
    assert useStringLeft("abc123def", "def") == "abc123"
    assert useStringLeft("abc123def", "abc") == ""
    assert useStringLeft("abc123def", "123") == "abc"


def test_get_right():
    assert useStringRight("abc123def", "abc") == "123def"
    assert useStringRight("abc123def", "def") == ""
    assert useStringRight("abc123def", "123") == "def"
