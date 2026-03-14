from typing import TypeVar, Sequence, Callable, Optional

T = TypeVar('T')


def find(arr: Sequence[T], predicate: Callable[[T], bool], default: Optional[T] = None) -> Optional[T]:
    """
    Finds the first element in a sequence that satisfies a predicate function.

    Args:
        arr (Sequence[T]): The sequence to search.
        predicate (Callable[[T], bool]): A function that returns True for the desired element.
        default (Optional[T]): The value to return if no element is found. Defaults to None.

    Returns:
        Optional[T]: The first element that satisfies the predicate, or default if not found.

    Examples:
        >>> find([1, 2, 3, 4], lambda x: x > 2)
        3
        >>> find([1, 2, 3], lambda x: x > 10, default=0)
        0
        >>> find([], lambda x: x > 0)
        None
    """
    for item in arr:
        if predicate(item):
            return item
    return default