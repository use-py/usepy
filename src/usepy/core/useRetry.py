import functools
import time
import asyncio


class MaxRetryError(Exception):
    pass


class useRetry(object):
    """
    用于函数重试的装饰器，支持异步函数

    :param max_retry: 最大重试次数
    :param retry_interval: 重试间隔
    :param retry_exceptions: 重试异常

    >>> @useRetry(max_retry=3, retry_interval=1)
    ... def test():
    ...     print('test')
    ...     raise Exception('test')
    """

    def __init__(self, max_retry=3, retry_interval=1, retry_exceptions=None):
        self.max_retry = max_retry
        self.retry_interval = retry_interval
        self.retry_exceptions = retry_exceptions or (Exception,)

    def __call__(self, func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retry = 0
            while retry < self.max_retry:
                try:
                    return func(*args, **kwargs)
                except self.retry_exceptions as e:
                    retry += 1
                    if retry >= self.max_retry:
                        raise MaxRetryError(f"Max retry {self.max_retry} times，Error reason: {e}")
                    time.sleep(self.retry_interval)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):

            retry = 0
            while retry < self.max_retry:
                try:
                    return await func(*args, **kwargs)
                except self.retry_exceptions as e:
                    retry += 1
                    if retry >= self.max_retry:
                        raise MaxRetryError(f"Max retry {self.max_retry} times，Error reason: {e}")
                    await asyncio.sleep(self.retry_interval)

        wrapper_func = async_wrapper if asyncio.iscoroutinefunction(func) else wrapper
        return wrapper_func
