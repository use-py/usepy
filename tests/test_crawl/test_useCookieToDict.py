from usepy import useCookieToDict


def test_cookie_to_dict():
    cookie_str = "code=1000; name=miclon; UID=359FEA9A6F1C7E97BFE909A1A700F5DE"
    assert useCookieToDict(cookie_str) == {
        "code": "1000",
        "name": "miclon",
        "UID": "359FEA9A6F1C7E97BFE909A1A700F5DE",
    }
