from typing import Callable, List, TypeVar

T = TypeVar('T')


def some(array: List[T], fn: Callable[[T], bool]) -> bool:
    """
    Checks if at least one element in the given array satisfies the provided condition function.

    Args:
        array (List[T]): The input array to be checked.
        fn (Callable[[T], bool]): The condition function that takes an element and returns a boolean value.
            If the function returns True for any element, the function will return True.

    Returns:
        bool: True if at least one element satisfies the condition function, False otherwise.

    Example:
        >>> nums = [1, 2, 3, 4, 5]
        >>> is_even = lambda x: x % 2 == 0
        >>> some(nums, is_even)
        True
        >>> is_negative = lambda x: x < 0
        >>> some(nums, is_negative)
        False
    """
    from functools import reduce
    from operator import or_

    return reduce(or_, [fn(element) for element in array])
