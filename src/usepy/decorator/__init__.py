from .retry import Retry as retry
from .catch_error import catch_error
from .singleton import singleton
from .throttle import Throttle as throttle
from .debounce import debounce, Debounce
from .memoize import memoize

__all__ = [
    "retry",
    "catch_error",
    "singleton",
    "throttle",
    # New decorators
    "debounce",
    "Debounce",
    "memoize",
]