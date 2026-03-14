from typing import TypeVar, Sequence, Optional

T = TypeVar('T')


def nth(arr: Sequence[T], n: int, default: Optional[T] = None) -> Optional[T]:
    """
    Gets the element at index n of a sequence. Supports negative indices.

    Args:
        arr (Sequence[T]): The sequence to query.
        n (int): The index of the element to return. Negative indices count from the end.
        default (Optional[T]): The value to return if index is out of bounds. Defaults to None.

    Returns:
        Optional[T]: The element at index n, or default if out of bounds.

    Examples:
        >>> nth([1, 2, 3, 4, 5], 1)
        2
        >>> nth([1, 2, 3, 4, 5], -1)
        5
        >>> nth([1, 2, 3], 10, default=0)
        0
        >>> nth([], 0)
        None
    """
    if not arr:
        return default

    try:
        return arr[n]
    except IndexError:
        return default