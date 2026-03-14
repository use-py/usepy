from typing import TypeVar, Sequence, List

T = TypeVar('T')


def take(arr: Sequence[T], n: int = 1) -> List[T]:
    """
    Takes the first n elements from a sequence.

    Args:
        arr (Sequence[T]): The sequence to take from.
        n (int): The number of elements to take. Defaults to 1.

    Returns:
        List[T]: A new list with the first n elements.

    Examples:
        >>> take([1, 2, 3, 4, 5], 2)
        [1, 2]
        >>> take([1, 2, 3], 0)
        []
        >>> take([1, 2, 3], 10)
        [1, 2, 3]
    """
    return list(arr[:n])


def take_right(arr: Sequence[T], n: int = 1) -> List[T]:
    """
    Takes the last n elements from a sequence.

    Args:
        arr (Sequence[T]): The sequence to take from.
        n (int): The number of elements to take from the end. Defaults to 1.

    Returns:
        List[T]: A new list with the last n elements.

    Examples:
        >>> take_right([1, 2, 3, 4, 5], 2)
        [4, 5]
        >>> take_right([1, 2, 3], 0)
        []
        >>> take_right([1, 2, 3], 10)
        [1, 2, 3]
    """
    if n <= 0:
        return []
    return list(arr[-n:]) if n < len(arr) else list(arr)