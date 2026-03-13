from typing import List, Callable, TypeVar
from functools import reduce
from operator import and_

T = TypeVar('T')


def every(array: List[T], fn: Callable[[T], bool]) -> bool:
    """
    Checks if every element in the given array satisfies the provided condition function.

    Args:
        array (List[T]): The input array to be checked.
        fn (Callable[[T], bool]): The condition function that takes an element of the array as input
            and returns a boolean value indicating whether the element satisfies the condition or not.

    Returns:
        bool: True if every element in the array satisfies the condition function, False otherwise.

    Example:
        >>> is_even = lambda x: x % 2 == 0
        >>> every([2, 4, 6, 8], is_even)
        True
        >>> every([1, 3, 5, 7], is_even)
        False
        >>> every([],lambda x: x > 0)
        True
    """
    return reduce(and_, [fn(element) for element in array], True)
