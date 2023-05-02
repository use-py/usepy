import functools
import threading


def useSingleton(cls):
    """
    单例模式装饰器
    >>> @useSingleton
    >>> class MyClass: pass
    """
    _instance = {}
    useSingleton.__lock = threading.Lock()

    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]
        with useSingleton.__lock:
            if cls not in _instance:
                _instance[cls] = cls(*args, **kwargs)
            return _instance[cls]

    return _singleton
