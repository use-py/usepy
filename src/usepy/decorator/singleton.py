import functools
import threading
from typing import Any, Callable, Type, TypeVar

T = TypeVar("T")


def singleton(cls: Type[T]) -> Callable[..., T]:
    """
    A decorator for implementing the Singleton pattern.

    This decorator ensures that only one instance of the decorated class is created,
    and subsequent calls to the class constructor return the same instance.

    Args:
        cls (Type[T]): The class to be decorated.

    Returns:
        Callable[..., T]: A function that returns the singleton instance of the class.

    Example:
        >>> @singleton
        ... class MyClass:
        ...     def __init__(self, value):
        ...         self.value = value
        ...
        >>> instance1 = MyClass(42)
        >>> instance2 = MyClass(24)
        >>> print(instance1.value)
        42
        >>> print(instance1 is instance2)
        True
    """
    _instances: dict[Type[T], T] = {}
    _lock = threading.Lock()

    @functools.wraps(cls)
    def _singleton(*args: Any, **kwargs: Any) -> T:
        if cls not in _instances:
            with _lock:
                if cls not in _instances:
                    _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return _singleton
