import asyncio
from functools import wraps
import time


class Throttle:
    """Throttle Decorator

    This decorator is used to limit the rate at which a function can be called.
    It ensures that the function is not called more than once in a given time period.

    Args:
        delay (int): The time period in seconds within which the function can be called.
    """

    def __init__(self, delay: int):
        self.delay = delay
        self.last_called = 0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal self
            current_time = time.time()
            if current_time - self.last_called >= self.delay:
                result = func(*args, **kwargs)
                self.last_called = current_time
                return result

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            return wrapper(*args, **kwargs)

        wrapper_func = async_wrapper if asyncio.iscoroutinefunction(func) else wrapper

        return wrapper_func
