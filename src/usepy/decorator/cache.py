import functools


def cached_property(func):
    """
    缓存属性装饰器
    >>> @cached_property
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
