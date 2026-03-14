from typing import TypeVar, Sequence, Callable

T = TypeVar('T')


def find_index(arr: Sequence[T], predicate: Callable[[T], bool]) -> int:
    """
    Finds the index of the first element in a sequence that satisfies a predicate function.

    Args:
        arr (Sequence[T]): The sequence to search.
        predicate (Callable[[T], bool]): A function that returns True for the desired element.

    Returns:
        int: The index of the first element that satisfies the predicate, or -1 if not found.

    Examples:
        >>> find_index([1, 2, 3, 4], lambda x: x > 2)
        2
        >>> find_index([1, 2, 3], lambda x: x > 10)
        -1
        >>> find_index([], lambda x: x > 0)
        -1
    """
    for i, item in enumerate(arr):
        if predicate(item):
            return i
    return -1