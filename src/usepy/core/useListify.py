import functools
from typing import Callable


def useListify(collection: Callable = list):
    """
    将函数的返回值转换为列表。
    :param collection: 转换函数, 默认为list
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return collection(res)

        return wrapper

    return decorator
