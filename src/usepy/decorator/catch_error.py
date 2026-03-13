import functools
import logging
from typing import Callable, Any, Optional, TypeVar

T = TypeVar("T")


def catch_error(
        return_val: Optional[T] = None,
) -> Callable[[Callable[..., T]], Callable[..., Optional[T]]]:
    """
    Catch Error Decorator

    This decorator function is used to catch exceptions that may occur during the execution of a function.
    If an exception occurs, it will log the exception using the `logging.debug` method and return the specified `return_val`.

    Args:
        return_val (Optional[T]): The value to be returned if an exception occurs during the execution of the decorated function.
                                  If not provided, it defaults to `None`.

    Returns:
        Callable[[Callable[..., T]], Callable[..., Optional[T]]]: A decorator function that takes a function as input
                                                                  and returns a new function that catches exceptions.

    Example:
        >>> import logging
        >>> logging.basicConfig(level=logging.DEBUG)
        >>>
        >>> @catch_error(return_val=0)
        ... def divide(a, b):
        ...     return a / b
        ...
        >>> divide(10, 2)
        5.0
        >>> divide(10, 0)
        Error occurred: division by zero
        0
    """

    def decorator(func: Callable[..., T]) -> Callable[..., Optional[T]]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Optional[T]:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.debug(f"Error occurred: {e}")
                return return_val

        return wrapper

    return decorator
