import asyncio
from typing import Callable


def is_async_function(func: Callable) -> bool:
    """
    check if the function is an async function
    >>> is_async_function(lambda x: x)
    False
    """

    return asyncio.iscoroutinefunction(func)
