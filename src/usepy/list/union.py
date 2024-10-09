from typing import TypeVar, Iterable
from usepy.list.uniq import uniq

T = TypeVar('T')


def union(*lsts: Iterable[T]) -> list[T]:
    """
    Creates a list of unique values from all given iterables.

    This function takes any number of iterables, merges them into a single iterable, and returns a new list
    containing only the unique values from the merged iterable.

    Args:
        *lsts (Iterable[T]): The iterables to merge and filter for unique values.

    Returns:
        list[T]: A new list of unique values.

    Example:
        >>> array1 = [1, 2, 3]
        >>> array2 = [3, 4, 5]
        >>> array3 = [5, 6, 7]
        >>> union(array1,array2,array3)
        [1, 2, 3, 4, 5, 6, 7]
    """
    merged = [item for arr in lsts for item in arr]
    return uniq(merged)
