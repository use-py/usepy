import functools
from threading import Lock


def useSynchronized(func):
    """
    线程安全装饰器
    >>> @useSynchronized
    >>> def demo(x):
    >>>     return x
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        lock = vars(func).get("_synchronized_lock", None)
        if lock is None:
            lock = vars(func).setdefault("_synchronized_lock", Lock())
        with lock:
            return func(*args, **kwargs)

    return wrapper

