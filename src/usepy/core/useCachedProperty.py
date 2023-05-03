import functools


def useCachedProperty(func):
    """
    带有缓存属性装饰器
    >>> @useCachedProperty
    >>> def demo(self):
    >>>     return 1
    """
    prop_name = '_{}'.format(func.__name__)

    @functools.wraps(func)
    def wrapped_func(self, *args, **kwargs):
        if not hasattr(self, prop_name):
            setattr(self, prop_name, func(self, *args, **kwargs))
        return getattr(self, prop_name)

    return property(wrapped_func)
