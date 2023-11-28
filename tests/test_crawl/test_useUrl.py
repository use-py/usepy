from usepy import useURL


def test_url():
    url = useURL("https://www.google.com/search?q=usepy&ie=utf-8")
    assert url.scheme == "https"
    assert url.query == "q=usepy&ie=utf-8"
    assert url.query_dict == {"q": "usepy", "ie": "utf-8"}
    assert url.path == "/search"

    url = useURL(
        "https://www.google.com/search?s=%E6%88%91%E6%98%AFusepy&s=usepy2&ie=utf-8"
    )
    assert url.scheme == "https"
    assert url.netloc == "www.google.com"
    assert url.query_dict == {"s": ["我是usepy", "usepy2"], "ie": "utf-8"}
    assert url.path == "/search"
    assert url.decode == "https://www.google.com/search?s=我是usepy&s=usepy2&ie=utf-8"
