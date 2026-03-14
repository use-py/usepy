import asyncio
from functools import wraps
from typing import Any, Callable, Dict, Tuple
import hashlib
import pickle


def memoize(func: Callable) -> Callable:
    """
    Memoize Decorator

    Caches the results of function calls based on arguments.
    Subsequent calls with the same arguments return the cached result.

    Args:
        func (Callable): The function to memoize.

    Returns:
        Callable: The memoized function.

    Example:
        >>> @memoize
        ... def expensive_computation(n):
        ...     print(f"Computing {n}...")
        ...     return n * n
        >>> expensive_computation(5)
        Computing 5...
        25
        >>> expensive_computation(5)  # Returns cached result
        25
    """
    cache: Dict[str, Any] = {}

    def _make_key(args: Tuple, kwargs: Dict) -> str:
        """Generate a unique key for the given arguments."""
        key_data = pickle.dumps((args, frozenset(kwargs.items())))
        return hashlib.md5(key_data).hexdigest()

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = _make_key(args, kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        key = _make_key(args, kwargs)
        if key not in cache:
            cache[key] = await func(*args, **kwargs)
        return cache[key]

    # Add method to clear cache
    wrapper.cache_clear = lambda: cache.clear()
    async_wrapper.cache_clear = lambda: cache.clear()

    return async_wrapper if asyncio.iscoroutinefunction(func) else wrapper