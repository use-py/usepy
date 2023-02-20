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
