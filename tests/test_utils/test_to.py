from usepy import useTo


def test_to_dict():
    assert useTo.cookie_to_dict(
        "code=1000; name=miclon; UID=359FEA9A6F1C7E97BFE909A1A700F5DE"
    ) == {
               "code": "1000",
               "name": "miclon",
               "UID": "359FEA9A6F1C7E97BFE909A1A700F5DE",
           }

    assert useTo.headers_to_dict(
        """
        pragma: no-cache
referer: https://github.com/
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0
        """) == {
               "pragma": "no-cache",
               "referer": "https://github.com/",
               "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0",
           }
    assert useTo.data_to_dict("code=1000&name=miclon&UID=359FEA9A6F1C7E97BFE909A1A700F5DE") == {
        "code": "1000",
        "name": "miclon",
        "UID": "359FEA9A6F1C7E97BFE909A1A700F5DE",
    }


def test_to_string():
    assert useTo.to_string("test") == "test"
    assert useTo.to_string(b"test") == "test"
    assert useTo.to_string(1000) == "1000"
    assert useTo.to_string(1000.0) == "1000.0"
    assert useTo.to_string(True) == "True"
    assert useTo.to_string(None) == "None"
    assert useTo.to_string([1, 2, 3]) == "[1, 2, 3]"
    assert useTo.to_string({"code": 1000}) == "{'code': 1000}"
