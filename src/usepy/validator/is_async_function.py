import asyncio
from typing import Callable, Any


def is_async_function(func: Callable[..., Any]) -> bool:
    """
    Check if the function is an async function.

    Args:
        func (Callable[..., Any]): The function to check.

    Returns:
        bool: True if the function is async, False otherwise.

    Examples:
        >>> async def async_func(): pass
        >>> is_async_function(async_func)
        True
        >>> is_async_function(lambda x: x)
        False
    """
    return asyncio.iscoroutinefunction(func)
