from usepy.decorator import retry, catch_error, singleton, throttle
import time


def test_retry():
    count = 0

    @retry(max_attempts=3, retry_interval=0.1)
    def failing_function():
        nonlocal count
        count += 1
        if count < 3:
            raise ValueError("Test error")
        return "Success"

    assert failing_function() == "Success"


def test_catch_error():
    @catch_error(return_val="Default")
    def error_function():
        raise ValueError("Test error")

    assert error_function() == "Default"


def test_singleton():
    @singleton
    class SingletonClass:
        pass

    instance1 = SingletonClass()
    instance2 = SingletonClass()
    assert instance1 is instance2


def test_throttle():
    call_count = 0

    @throttle(delay=0.1)
    def throttled_function():
        nonlocal call_count
        call_count += 1

    throttled_function()
    throttled_function()
    time.sleep(0.2)
    throttled_function()

    assert call_count == 2
