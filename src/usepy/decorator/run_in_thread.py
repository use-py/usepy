import functools
import threading


def run_in_thread(func):
    """
    函数在调用的时候会运行在单独的线程中

    >>> @run_in_thread
    >>> def runner():
    >>>     pass
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

    return wrapper
