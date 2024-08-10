from typing import TypeVar, Sequence

T = TypeVar('T')


def uniq(lst: Sequence[T]) -> list[T]:
    """
    Returns a new list containing only the unique elements from the input sequence.

    Args:
        lst (Sequence[T]): The input sequence.

    Returns:
        list[T]: A new list containing only the unique elements from the input sequence.

    Example:
        >>> uniq([1, 2, 3, 2, 1])
        [1, 2, 3]
    """
    return list(set(lst))
