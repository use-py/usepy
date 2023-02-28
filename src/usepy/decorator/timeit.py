import functools
import time
import logging

logger = logging.getLogger(__name__)


def time_it(func):
    """
    计时装饰器
    """

    @functools.wraps(func)
    def _timer(*args, **kwargs):
        t0 = time.perf_counter()
        back = func(*args, **kwargs)
        t1 = time.perf_counter()
        logger.debug(f"{func.__name__} took {t1 - t0:.0f} seconds")
        return back

    return _timer
