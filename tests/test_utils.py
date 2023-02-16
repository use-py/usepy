from usepy.utils import *


def test_user_agent():
    assert useUserAgent.get() in useUserAgent.PC_USER_AGENTS
    assert useUserAgent.get(False) in useUserAgent.MOBILE_USER_AGENTS


def test_use_timer():
    _timer = useTimer("test", lambda: print("test"), 1)
    assert _timer.name == "test"
    assert _timer.alive() is False
    _timer.scheduler()
    assert _timer.alive() is True
    _timer.cancel()


def test_import():
    module, _ = useImport("this")
    assert module.__name__ == "this"
    assert _ is None
    module, func = useImport("usepy.utils:useUserAgent")
    assert module.__name__ == "usepy.utils"
    assert func.__name__ == "usepy.utils.useragent"


def test_cookie_to_dict():
    cookie_str = "code=1000; name=miclon; UID=359FEA9A6F1C7E97BFE909A1A700F5DE"
    assert useCookieToDict(cookie_str) == {
        "code": "1000",
        "name": "miclon",
        "UID": "359FEA9A6F1C7E97BFE909A1A700F5DE",
    }


def test_header_to_dict():
    header_str = """sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"
    sec-ch-ua-platform: "macOS"
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"""
    assert useHeadersToDict(header_str) == {
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        "sec-ch-ua-platform": '"macOS"',
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }


def test_unique_id():
    assert len(useUniqueId()) == 32
