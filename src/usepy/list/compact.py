from typing import TypeVar, Sequence

T = TypeVar('T')


def compact(arr: Sequence[T]) -> Sequence[T]:
    """
    Removes falsey values (False, None, 0, '', [], {}) from a sequence.

    Args:
        arr (Sequence[T]): The input sequence to remove falsey values.

    Returns:
        Sequence[T]: A new sequence with all falsey values removed.

    Example:
        >>> compact([0, 1, False, 2, '', 3, None, 4, {}, 5])
        [1, 2, 3, 4, 5]
    """
    return [item for item in arr if item]
