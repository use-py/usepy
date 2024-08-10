from typing import TypeVar

from usepy.list.flatten import flatten

T = TypeVar("T")


def flatten_deep(lst: list[T]) -> list:
    """
    Flattens all depths of a nested array.

    Args:
        lst (list[T]): The array to flatten.

    Returns:
        list: A new array that has been flattened.

    Example:
        >>> flatten_deep([1, [2, [3]], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
    """
    return flatten(lst, float("inf"))
