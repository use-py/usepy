import functools
import time


def useTimeIt(func):
    """
    计时装饰器
    """

    @functools.wraps(func)
    def _timer(*args, **kwargs):
        t0 = time.perf_counter()
        back = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"{func.__name__} took {t1 - t0:.0f} seconds")
        return back

    return _timer
