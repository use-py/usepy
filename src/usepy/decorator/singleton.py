import functools
import threading


def singleton(cls):
    """
    单例模式装饰器
    >>> @singleton
    >>> class MyClass: pass
    """
    _instance = {}
    singleton.__lock = threading.Lock()

    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]
        with singleton.__lock:
            if cls not in _instance:
                _instance[cls] = cls(*args, **kwargs)
            return _instance[cls]

    return _singleton
