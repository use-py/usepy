from typing import TypeVar, Sequence

T = TypeVar("T")


def last(array: Sequence[T]) -> T | None:
    """
    Gets the last element of `array`.

    :param array: The array to query.
    :type array: Sequence[T]
    :return: Returns the last element of `array`.
    :rtype: T | None

    :Example:

    >>> last([1, 2, 3])
    3
    """
    return array[-1] if array else None
