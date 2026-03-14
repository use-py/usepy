import asyncio
from functools import wraps
import time
import threading


class Debounce:
    """
    Debounce Decorator

    Delays the function execution until after a specified time has elapsed
    since the last call. Useful for rate-limiting rapid function calls.

    Args:
        delay (float): The delay in seconds to wait before executing.

    Example:
        >>> @debounce(delay=0.5)
        ... def search(query):
        ...     print(f"Searching for: {query}")
    """

    def __init__(self, delay: float):
        self.delay = delay
        self.timer = None
        self.lock = threading.Lock()

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with self.lock:
                if self.timer:
                    self.timer.cancel()
                
                def execute():
                    return func(*args, **kwargs)
                
                self.timer = threading.Timer(self.delay, execute)
                self.timer.start()

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            with self.lock:
                if self.timer:
                    self.timer.cancel()
                
                async def execute():
                    return await func(*args, **kwargs)
                
                self.timer = threading.Timer(self.delay, lambda: asyncio.run(execute()))
                self.timer.start()

        return async_wrapper if asyncio.iscoroutinefunction(func) else wrapper


def debounce(delay: float):
    """
    Debounce decorator factory.

    Args:
        delay (float): The delay in seconds to wait before executing.

    Returns:
        Debounce: The debounce decorator.

    Example:
        >>> @debounce(delay=0.5)
        ... def save_data(data):
        ...     print(f"Saving: {data}")
    """
    return Debounce(delay)