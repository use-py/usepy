import functools
import logging
import pdb


def except_debug(func):
    """
    跟踪调试函数装饰器
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            pdb.set_trace()
            logging.debug(e)
            return func(*args, **kwargs)

    return wrapper
