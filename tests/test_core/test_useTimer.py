from usepy import useTimer


def test_use_timer():
    _timer = useTimer("test", lambda: print("test"), 1)
    assert _timer.name == "test"
    assert _timer.alive() is False
    _timer.scheduler()
    assert _timer.alive() is True
    _timer.cancel()
