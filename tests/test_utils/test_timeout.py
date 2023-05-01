from usepy import useTimeoutFn, useTimeout
import time


def test_useTimeoutFn():
    def callback():
        callback.called = True

    callback.called = False
    timeout = useTimeoutFn(0.1, callback)
    assert timeout.is_pending is False
    timeout.start()
    assert timeout.is_pending is True
    time.sleep(0.2)
    assert callback.called is True
    assert timeout.is_pending is True
    timeout.stop()
    assert timeout.is_pending is False


def test_useTimeout():
    def callback():
        callback.called = True

    callback.called = False
    timeout = useTimeout(0.1)
    timeout._cb = callback
    timeout.start()
    time.sleep(0.2)
    assert callback.called is True
