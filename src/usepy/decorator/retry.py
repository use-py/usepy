import asyncio
import functools
import time


class MaxRetryError(Exception):
    pass


class Retry(object):
    """
    Decorator for retrying a function, supports asynchronous functions

    :param max_attempts: maximum retry attempts
    :param retry_interval: retry interval
    :param retry_exceptions: retry exceptions

    >>> @retry(max_attempts=3, retry_interval=1)
    ... def test():
    ...     print('test')
    ...     raise Exception('test')
    """

    def __init__(self, max_attempts=3, retry_interval=1, retry_exceptions=None):
        self.max_attempts = max_attempts
        self.retry_interval = retry_interval
        self.retry_exceptions = retry_exceptions or (Exception,)

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retry = 0
            while retry < self.max_attempts:
                try:
                    return func(*args, **kwargs)
                except self.retry_exceptions as e:
                    retry += 1
                    if retry >= self.max_attempts:
                        raise MaxRetryError(
                            f"Max retry {self.max_attempts} times，Error reason: {e}"
                        )
                    time.sleep(self.retry_interval)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            retry = 0
            while retry < self.max_attempts:
                try:
                    return await func(*args, **kwargs)
                except self.retry_exceptions as e:
                    retry += 1
                    if retry >= self.max_attempts:
                        raise MaxRetryError(
                            f"Max retry {self.max_attempts} times，Error reason: {e}"
                        )
                    await asyncio.sleep(self.retry_interval)

        wrapper_func = async_wrapper if asyncio.iscoroutinefunction(func) else wrapper
        return wrapper_func
