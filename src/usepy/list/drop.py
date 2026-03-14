from typing import TypeVar, Sequence, List

T = TypeVar('T')


def drop(arr: Sequence[T], n: int = 1) -> List[T]:
    """
    Drops the first n elements from a sequence.

    Args:
        arr (Sequence[T]): The sequence to drop from.
        n (int): The number of elements to drop. Defaults to 1.

    Returns:
        List[T]: A new list without the first n elements.

    Examples:
        >>> drop([1, 2, 3, 4, 5], 2)
        [3, 4, 5]
        >>> drop([1, 2, 3], 0)
        [1, 2, 3]
        >>> drop([1, 2, 3], 10)
        []
    """
    return list(arr[n:])


def drop_right(arr: Sequence[T], n: int = 1) -> List[T]:
    """
    Drops the last n elements from a sequence.

    Args:
        arr (Sequence[T]): The sequence to drop from.
        n (int): The number of elements to drop from the end. Defaults to 1.

    Returns:
        List[T]: A new list without the last n elements.

    Examples:
        >>> drop_right([1, 2, 3, 4, 5], 2)
        [1, 2, 3]
        >>> drop_right([1, 2, 3], 0)
        [1, 2, 3]
        >>> drop_right([1, 2, 3], 10)
        []
    """
    if n <= 0:
        return list(arr)
    return list(arr[:-n]) if n < len(arr) else []