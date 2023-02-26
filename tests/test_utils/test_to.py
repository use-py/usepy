from usepy import useTo


def test_to_string():
    assert useTo.string("test") == "test"
    assert useTo.string(b"test") == "test"
    assert useTo.string(1000) == "1000"
    assert useTo.string(1000.0) == "1000.0"
    assert useTo.string(True) == "True"
    assert useTo.string(None) == "None"
    assert useTo.string([1, 2, 3]) == "[1, 2, 3]"
    assert useTo.string({"code": 1000}) == "{'code': 1000}"


def test_to_camel():
    assert useTo.camel("test") == "test"
    assert useTo.camel("test-case") == "testCase"
    assert useTo.camel("test_case", char="_") == "testCase"


def test_to_snake():
    assert useTo.snake("test") == "test"
    assert useTo.snake("testCase") == "test_case"
    assert useTo.snake("testCase", char="-") == "test-case"
